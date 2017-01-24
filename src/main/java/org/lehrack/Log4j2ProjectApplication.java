package org.lehrack;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class Log4j2ProjectApplication {

	private final static Logger log = LogManager.getLogger();
	
	public static void main(String[] args) {
		SpringApplication.run(Log4j2ProjectApplication.class, args);
		System.out.println("Log4J2 says hello ...");
		log.info("Log4J2 says hello ...");
	}
}
