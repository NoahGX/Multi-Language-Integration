import System.Environment (getArgs)

-- Function to subtract each element in list from 255
subtractElem :: [Int] -> [Int]
subtractElem [] = []
subtractElem (x:xs) = (255 - x) : subtractElem xs

main :: IO ()
main = do
    args <- getArgs                         -- Convert arguments to strings
    let nums = map read args :: [Int]       -- Convert strings to integers
        output = subtractElem nums          -- Call function
        outputStr = map show output         -- Convert result to string list
        result = unwords outputStr          -- Convert result back to string
    putStrLn result                         -- Print result