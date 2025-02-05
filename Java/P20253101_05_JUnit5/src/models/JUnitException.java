package models;

class JUnitException {
	void testException() throws Exception {
		throw new Exception("Eccezione JUnit");
	}

	public static void main(String[] args) throws Exception {
		JUnitException ex = new JUnitException();
		ex.testException();
	}
}
