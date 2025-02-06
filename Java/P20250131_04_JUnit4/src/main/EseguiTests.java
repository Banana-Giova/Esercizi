package main;
import org.junit.platform.suite.api.SelectClasses;
import org.junit.platform.suite.api.Suite;

import models.*;


@Suite
@SelectClasses({CalcolatriceTest.class, TestStringhe.class})
public class EseguiTests {

}