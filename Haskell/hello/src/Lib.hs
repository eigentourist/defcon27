-- Hacking With Monads:
-- Functional Programming for the Blue Team
-- A Def Con 27 Workshop August 10, 2019

-- Hello, World!

module Lib
    ( hello
    ) where

hello :: IO ()
hello = putStrLn "Hello, World!"
