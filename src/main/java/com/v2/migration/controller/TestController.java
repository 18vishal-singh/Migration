package com.v2.migration.controller;

import com.v2.migration.services.HelloService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class TestController {
    @RequestMapping("/test1")
    public String firstPage() {
        return "Hello, this is test1";
    }

    @Autowired
    @Qualifier("helloServicePython")
    private HelloService service;

    @RequestMapping("/hello")
    public String index() {
        return service.getHello();
    }
}
