package com.v2.migration.services;

import org.python.core.Py;
import org.python.core.PyObject;
import org.python.core.PyString;
import org.python.core.PySystemState;
import org.python.util.PythonInterpreter;
import org.springframework.beans.factory.FactoryBean;


public class HelloServiceFactory implements FactoryBean<HelloService> {

    @Override
    public HelloService getObject() throws Exception {

        //The python classpath is usually set by environment variable
//or included in the java project classpath but it can also be set
// programmatically.  Here I hard code it just for the example.
        //This is not required if we use jython standalone JAR
//        PySystemState systemState = Py.getSystemState();
//        systemState.path.append(new PyString("lib/"));

        //Here is the actual code that interprets our python file.
        PythonInterpreter interpreter = new PythonInterpreter();
        interpreter.execfile("python/HelloServicePython.py");
        PyObject buildingObject = interpreter.get("HelloServicePython").__call__();

//Cast the created object to our Java interface
        return (HelloService) buildingObject.__tojava__(HelloService.class);
    }

    @Override
    public Class<?> getObjectType() {
        return HelloService.class;
    }

}
