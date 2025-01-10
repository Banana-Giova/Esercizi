package threads;

public class ThreadChecker {
	public void thread_state(Thread thread) {
		System.out.println(thread.getName());
		System.out.println(thread.getState());
	}
}