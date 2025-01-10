package threads;

public class ThreadChecker {
	public void thread_state(Thread thread) {
		System.out.println(thread.getState());
		System.out.println(thread.getName());
	}
	
	public void thread_mod(Thread thread, String new_name) {
		thread.setName(new_name);
	}
}