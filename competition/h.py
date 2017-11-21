
--this isn't Python but Haskell (you're not expected to understand this so feel free to ignore this code)
--Can't upload .hs files so I renamed this to .py

shuffle cards =
   let len = length cards
       len_half = (if even len
                   then (len `quot` 2)
                   else (len `quot` 2) + 1)
       s1 = take len_half cards
       s2 = drop len_half cards
       almost_ans = concat $ zipWith (\a b -> [a, b]) s1 s2
   in if even len then almost_ans else almost_ans ++ [last s1]
   --in (s1, s2)

x = shuffle ["ACE", "KING", "QUEEN", "JACK"]
y = shuffle ["SKIP", "DRAW-TWO", "REVERSE", "WILD", "WILD_DRAW-FOUR"]
