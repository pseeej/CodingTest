package com.ssafy;

import java.util.Scanner;

public class b2556 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int maxnum = 0;
		int row = 0, col = 0;
		
		for(int i=0;i<9;i++) {
			for(int j=0;j<9;j++) {
				int tmp = sc.nextInt();
				if (maxnum < tmp) {
					row = i;
					col = j;
					maxnum = tmp;
				}
			}
		}
		System.out.println(maxnum);
		System.out.printf("%d %d", row+1, col+1);
	}
}
