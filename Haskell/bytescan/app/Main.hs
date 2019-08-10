-- Hacking With Monads:
-- Functional Programming for the Blue Team
-- A Def Con 27 Workshop August 10, 2019

-- Recursively search all files inside a
-- path for a given sequence of bytes


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
        [x] -> scan x
        args -> scan $ show $ head args