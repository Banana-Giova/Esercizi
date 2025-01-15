
public class TryCatchFinally extends Thread{
	private long sleep;

	public TryCatchFinally(long sleep) {
		super();
		this.sleep = sleep;
	}

	@Override
	public void run() {
		try {
			System.out.println("Sono entrato nel Try!");
			Thread.sleep(sleep);
			throw new Exception();
		} catch (Exception e) {
			System.out.println("Sono entrato nel Catch!");
			e.printStackTrace();
		} finally {
			System.out.println("Sono entrato nel Finally!");
		}

	}


}
