package main;
import org.junit.platform.suite.api.SelectClasses;
import org.junit.platform.suite.api.Suite;

import models.*;


@Suite
@SelectClasses({CalcolatriceTest1.class, CalcolatriceTest2.class})
public class EseguiTests {

}