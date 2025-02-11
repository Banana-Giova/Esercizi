package com.spring.first.controller;
import java.util.Random;
import java.util.Arrays;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController //Indica a Spring che dovrà istanziare e gestire questa classe
@RequestMapping(path="/lotto")
public class LottoController {
	
	@GetMapping(path="/1")
	public int[] random_lotto() {
		int[] nums = new int[5];
		Random rng = new Random();
		int last_add = 0;
		
		while (true) {
			if (last_add <= 4) {
				int new_num = rng.nextInt(0, 100);
				if (Arrays.binarySearch(nums, new_num) < 0) {
					nums[last_add] = new_num;
					last_add++;
				}
			} else {
				return nums;
			}
		}
	}
	
}

