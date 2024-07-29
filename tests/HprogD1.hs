import System.Environment (getArgs)

-- Function to subtract 1 from each element in list
subtractBy1 :: [Int] -> [Int]
subtractBy1 [] = []
subtractBy1 (x:xs) = (x - 1) : subtractBy1 xs

main :: IO ()
main = do
    args <- getArgs                         -- Convert arguments to strings
    let nums = map read args :: [Int]       -- Convert strings to integers
        output = subtractBy1 nums           -- Call function
        outputStr = map show output         -- Convert result to string list
        result = unwords outputStr          -- Convert result back to string
    putStrLn result                         -- Print result