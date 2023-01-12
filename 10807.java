package com.ssafy;

import java.util.Scanner;

public class b10807 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();
		int[] nums = new int[N];
		for(int i=0;i<N;i++) {
			nums[i] = sc.nextInt();
		}
		
		int V = sc.nextInt();
		
		int cnt = 0;
		for(int i=0;i<N;i++) {
			if (nums[i] == V)
				cnt++;
		}
		
		System.out.println(cnt);
	}
}
