
module Lib
    ( hello,
      walk,
      scan,
      hashfiles
    ) where

import Control.Monad (forM_, when)
import Data.List (isSuffixOf)
import System.IO (isEOF)
import System.FilePath (joinPath)
import System.Directory.PathWalk (pathWalk)
import qualified Data.ByteString as BS
import qualified Data.ByteString.Lazy as BSL
import qualified Data.ByteString.Lazy.Search as SRCH
import Numeric (showHex)

-- https://www.fpcomplete.com/blog/2017/09/cryptographic-hashing-haskell
import System.IO (withBinaryFile, IOMode (ReadMode))
import Crypto.Hash (HashAlgorithm, Digest, SHA256, hash, hashInit, hashUpdate, hashFinalize)

hello :: IO ()
hello = putStrLn "Hello, World!"

-- Read-only list of bytes to scan for
srchstr = BS.pack [0x48, 0x8d, 0x45, 0xf0, 0x4c, 0x39, 0xf8, 0x72]


prettyPrint :: BS.ByteString -> String
prettyPrint = concat . map (flip showHex "") . BS.unpack


scanfile :: String -> IO Bool
scanfile path = do
    buffer <- BSL.readFile path
    let offsets = SRCH.indices srchstr buffer
    return (not (null offsets))


hashfile :: HashAlgorithm ha => FilePath -> IO (Digest ha)
hashfile fp = withBinaryFile fp ReadMode $ \h ->
  let loop context = do
        chunk <- BS.hGetSome h 4096
        if BS.null chunk
          then return $ hashFinalize context
          else loop $! hashUpdate context chunk
   in loop hashInit



walk :: String -> IO ()
walk path = pathWalk path $ \root dirs files -> do
    forM_ files $ \file ->
        when (".hs" `isSuffixOf` file) $ do
            putStrLn $ joinPath [root, file]


scan :: String -> IO ()
scan path = pathWalk path $ \root dirs files -> do
    forM_ files $ \file -> do
        result <- scanfile $ joinPath [root, file]
        when (result) $ do
            let msg = prettyPrint srchstr ++ " found in " ++ joinPath [root, file]
            putStrLn msg

hashfiles :: String -> IO ()
hashfiles path = pathWalk path $ \root dirs files -> do
    forM_ files $ \file -> do
        digest <- hashfile $ joinPath [root, file]
        putStrLn $ show (joinPath [root, file]) ++ " hash: " ++ show (digest :: Digest SHA256)

