package a3;

/**
 * Exception class for Assignment 3.
 *
 */
public class PpmException extends RuntimeException {
	/**
	 * Constant needed by the Serializable interface.
	 */
	private static final long serialVersionUID = 1L;

	/**
	 * Initialize this exception with the specified message.
	 * 
	 * @param msg the exception message
	 */
	public PpmException(String msg) {
		super(msg);
	}
}
