package main;
import org.junit.platform.suite.api.SelectClasses;
import org.junit.platform.suite.api.Suite;

import models.*;


@Suite
@SelectClasses({NumeroPariTest.class})
public class EseguiTests {

}