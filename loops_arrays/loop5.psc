Algoritmo loop5
	//Hacer un pseudoc—digo que imprima los numeros impares hasta el 100 y que imprima cuantos impares hay.
	w <- 0
	none <- 0
		Mientras w < 100
			si w % 2 != 0
				Imprimir w
				w <- w + 1
				none <- none + 1
			SiNo
				w <- w + 1
			FinSi
			
		FinMientras
		Imprimir "En total son: ", none
FinAlgoritmo
