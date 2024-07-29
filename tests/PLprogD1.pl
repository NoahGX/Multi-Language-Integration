% Function to write list elements separated by spaces
write_list([]).
write_list([Head]) :-
    write(Head).
write_list([Head|Tail]) :-
    write(Head),
    write(' '),
    write_list(Tail).

% Function to reverse list
reverse_list([], []).
reverse_list([Head|Tail], ReversedList) :-
    reverse_list(Tail, ReversedTail),
    append(ReversedTail, [Head], ReversedList).

main :-
    % Call functions
    read(InputList),
    reverse_list(InputList, ReversedList),
    write_list(ReversedList),
    nl, nl.