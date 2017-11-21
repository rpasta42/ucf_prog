

--data Tree = Tree Int [Tree] | Node Int

{-mk_tree nums =
   let isSibling  prev_num curr_num = if prev_num + 1 == curr_num then True

parse num_nodes k_our_node nums =
   let tree = mk_tree nums
-}


{-
construct xs = run' xs []

run' [] acc = acc
run' (x:xs) [] = run' xs [[x]]
run' (x:xs) acc@((grp@(y:ys)):rest) =
   if x == y+1
   then run' xs ((x:grp):rest)
   else run' xs ([x] : acc)
-}

construct xs = construct' xs []
construct' [] acc = acc
construct' (x:xs) ((num(y:ys):rest)



--run xs k =

--run' (x:y:xs) [] =


