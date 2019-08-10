-- Hacking With Monads:
-- Functional Programming for the Blue Team
-- A Def Con 27 Workshop August 10, 2019

-- Recursively generate hashes for all files
-- within a given file system path


module Lib
    ( 
        hashfiles
    ) where

import Control.Monad (forM_, when)
import Data.List (isSuffixOf)
import System.IO (isEOF)
import System.FilePath (joinPath)
import System.Directory.PathWalk (pathWalk)
import qualified Data.ByteString as BS

-- https://www.fpcomplete.com/blog/2017/09/cryptographic-hashing-haskell
import System.IO (withBinaryFile, IOMode (ReadMode))
import Crypto.Hash (HashAlgorithm, Digest, SHA256, hash, hashInit, hashUpdate, hashFinalize)

hashfile :: HashAlgorithm ha => FilePath -> IO (Digest ha)
hashfile fp = withBinaryFile fp ReadMode $ \h ->
  let loop context = do
        chunk <- BS.hGetSome h 4096
        if BS.null chunk
          then return $ hashFinalize context
          else loop $! hashUpdate context chunk
   in loop hashInit


hashfiles :: String -> IO ()
hashfiles path = pathWalk path $ \root dirs files -> do
    forM_ files $ \file -> do
        digest <- hashfile $ joinPath [root, file]
        putStrLn $ show (joinPath [root, file]) ++ " hash: " ++ show (digest :: Digest SHA256)

