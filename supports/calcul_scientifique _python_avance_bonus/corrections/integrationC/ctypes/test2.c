long factorielle(int n){
	long res = 1;
	while(n > 0){
		res *= n;
		n--;
	}
	return res;
}