% Function to reverse list
reverse_list([], []).
reverse_list([Head|Tail], ReversedList) :-
    reverse_list(Tail, ReversedTail),
    append(ReversedTail, [Head], ReversedList).

main :-
    % Call function
    read(InputList),
    reverse_list(InputList, ReversedList),
    write(ReversedList),
    nl, nl.