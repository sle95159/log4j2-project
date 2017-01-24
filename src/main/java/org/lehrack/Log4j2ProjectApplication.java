package org.lehrack;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class Log4j2ProjectApplication {

	public static void main(String[] args) {
		SpringApplication.run(Log4j2ProjectApplication.class, args);
		System.out.println("Log4J2 says hello ...");
	}
}
