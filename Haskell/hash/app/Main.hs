
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