male(john).
male(paul).
male(david).

female(mary).
female(lisa).

parent(john, paul).
parent(john, mary).
parent(lisa, paul).
parent(lisa, mary).
parent(paul, david).

father(X, Y) :-
    parent(X, Y),
    male(X).

mother(X, Y) :-
    parent(X, Y),
    female(X).

sibling(X, Y) :-
    parent(Z, X),
    parent(Z, Y),
    X \= Y.

grandparent(X, Y) :-
    parent(X, Z),
    parent(Z, Y).

:- initialization(main).

main :-
    write('FAMILY CHATBOT STARTED'), nl,
    write('Type a query like father(john,paul).'), nl,
    write('Type stop. to exit.'), nl,
    chat.

chat :-
    read(Q),
    ( Q = stop ->
        write('Goodbye!'), nl
    ;
        answer(Q),
        chat
    ).

answer(father(X, Y)) :-
    ( father(X, Y) ->
        write('Yes, correct.'), nl
    ;
        write('No, wrong.'), nl
    ).

answer(mother(X, Y)) :-
    ( mother(X, Y) ->
        write('Yes, correct.'), nl
    ;
        write('No, wrong.'), nl
    ).

answer(sibling(X, Y)) :-
    ( sibling(X, Y) ->
        write('Yes, they are siblings.'), nl
    ;
        write('No, they are not siblings.'), nl
    ).

answer(grandparent(X, Y)) :-
    ( grandparent(X, Y) ->
        write('Yes, correct.'), nl
    ;
        write('No, wrong.'), nl
    ).

answer(_) :-
    write('I do not understand.'), nl.