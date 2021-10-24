package com.v2.migration;

import com.v2.migration.services.HelloService;
import com.v2.migration.services.HelloServiceFactory;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;

@SpringBootApplication
public class MigrationApplication {

	public static void main(String[] args) {
		SpringApplication.run(MigrationApplication.class, args);
	}
	@Bean(name = "helloServiceFactory")
	public HelloServiceFactory helloFactory() {
		return new HelloServiceFactory();
	}

	@Bean(name = "helloServicePython")
	public HelloService helloServicePython() throws Exception {
		return helloFactory().getObject();
	}

}
