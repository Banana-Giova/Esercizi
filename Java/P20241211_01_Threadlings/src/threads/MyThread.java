package threads;

public class MyThread extends Thread {
    private long num;

    @SuppressWarnings("deprecation")
	public void run() {
        while (num --> 0) {
            System.out.println("Thread ID: "
                    + getId()+" => " + num);
        }
    }

    public MyThread(long num) {
        super();
        this.num=num;
    }

}
