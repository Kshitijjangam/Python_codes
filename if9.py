print('Enter 5 no')
A=int(input())
B=int(input())
C=int(input())
D=int(input())
E=int(input())
if A<B and A<C and A<D and A<E:
	print('First no is smallest')
elif B<A and B<C and B<D and B<E:
	print('Second no is smallest')
elif C<A and C<B and C<D and C<E:
	print('Third no is smallest')
elif D<A and D<B and D<C and D<E:
	print('Fourth no is smallest')
else:
	print('Fifth no is smallest')