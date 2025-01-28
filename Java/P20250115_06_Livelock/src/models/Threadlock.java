package models;

public class Threadlock extends Thread {
	private Threadlock thread;
	private String id;
	
	public Threadlock(Threadlock thread, String id) {
		this.thread = thread;
		this.id = id;
	}
	
	private void test() {
		System.out.println("Niente livelock!");
	}
	
	@Override
	public void run() {
		while (true) {
			System.out.println(this.id + " in attesa di " + this.thread.getName());
			if (this.thread.getState().equals(Thread.State.TERMINATED)) {
				break;
			} else {
				System.out.println(this.thread.getName() + " non disponibile, ritento!");
				try {
					Thread.sleep(2000);
				} catch (InterruptedException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
			}
		}
		test();
	}
}
