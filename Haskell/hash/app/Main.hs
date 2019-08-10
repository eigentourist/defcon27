-- Hacking With Monads:
-- Functional Programming for the Blue Team
-- A Def Con 27 Workshop August 10, 2019

-- Recursively generate hashes for all files
-- within a given file system path


module Main where

import System.Environment (getArgs, getProgName)
import Control.Exception
import System.Exit
import Lib

main :: IO ()
main = do
    args <- getArgs
    progName <- getProgName
    let exitMsg = "Usage: " ++ progName ++ " <path>"
    case args of
        [] -> do
            putStrLn exitMsg
        [x] -> hashfiles x
        args -> hashfiles $ show $ head args