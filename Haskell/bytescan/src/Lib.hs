
module Lib
    ( hello,
      scan
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


scan :: String -> IO ()
scan path = pathWalk path $ \root dirs files -> do
    forM_ files $ \file -> do
        result <- scanfile $ joinPath [root, file]
        when (result) $ do
            let msg = prettyPrint srchstr ++ " found in " ++ joinPath [root, file]
            putStrLn msg
