package a3;

import java.awt.Color;
import java.awt.Dimension;
import java.awt.FlowLayout;
import java.awt.image.BufferedImage;
import java.io.IOException;
import java.nio.file.FileSystems;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;

import javax.swing.ImageIcon;
import javax.swing.JFrame;
import javax.swing.JLabel;

/**
 * A reader of PPM ASCII images. This reader can handle blank lines and full
 * line comments, but cannot handle comments that appear on the same line as
 * image data. This reader has other limitations as described below.
 * 
 * <p>
 * The image header must be equal to {@code P3}, otherwise an exception is
 * thrown.
 * 
 * <p>
 * The image width and height must appear on the same line, otherwise an
 * exception is thrown.
 * 
 * <p>
 * The maximum value for each color must appear on a separate line, otherwise a
 * read error is likely to occur when reading in the pixel color data.
 * 
 * <p>
 * Each line of the image pixel data must contain a multiple of 3 unsigned
 * integer values.
 *
 */
public class PpmAsciiReader {

	/*
	 * DO NOT MODIFY THE FIELDS OF THIS CLASS
	 */
	private String magicNumber;
	private int height;
	private int width;
	private int maxValue;
	private SimpleImage img;

	/**
	 * Initializes a reader object that reads the PPM file located in the specified
	 * directory having the specified filename. If the specified file is readable
	 * then this constructor attempts to read the file as though it were a PPM
	 * plaintext color image file.
	 * 
	 * @param dir      the directory containing the PPM file
	 * @param filename the filename of the PPM file
	 * @throws PpmException if the PPM file is not readable, or if the file is
	 *                      readable but contains invalid or unexpected data
	 */
	public PpmAsciiReader(String dir, String filename) {
		/*
		 * THE CONSTRUCTOR IMPLEMENTS THE ALGORITHM IN THE ASSIGNMENT DOCUMENT
		 */
		Path path = FileSystems.getDefault().getPath("img", dir, filename);
		List<String> lines = null;
		try {
			lines = Files.readAllLines(path);
		} catch (IOException x) {
			throw new PpmException(x.getMessage());
		}
		List<String> next = readMagicNumber(lines);
		next = skipBlanksAndComments(next);
		next = readSize(next);
		next = skipBlanksAndComments(next);
		next = readMaxValue(next);
		this.img = new SimpleImage(this.width, this.height);
		next = skipBlanksAndComments(next);
		readPixels(next);
	}

	/**
	 * Attempts to read the magic number from the PPM file returning the remaining
	 * lines of the file.
	 * 
	 * @param lines the currently unread lines of text of the PPM file
	 * @return the remaining lines of text after reading the magic number
	 * @throws PpmException if the magic number is missing or is not equal to "P3"
	 */
	private List<String> readMagicNumber(List<String> lines) {
		if (lines.isEmpty()) {
			throw new PpmException("missing magic number");
		}
		// magic number is supposed to be the first thing in the file
		this.magicNumber = lines.get(0).trim();
		if (!this.magicNumber.equals("P3")) {
			throw new PpmException("unexpected magic number: " + this.magicNumber);
		}
		return lines.subList(1, lines.size());
	}

	/**
	 * Skips over a sequence of blank lines and lines of comments until some image
	 * information is found returning the remaining lines of the file.
	 * 
	 * @param lines the currently unread lines of text of the PPM file
	 * @return the remaining lines of text after reading a sequence of blank lines
	 *         and lines of comments
	 * @throws PpmException if lines is empty
	 */
	private List<String> skipBlanksAndComments(List<String> lines) {
		if (lines.isEmpty()) {
			throw new PpmException("unexpected end of file");
		}
		// examine each line until a non-blank non-comment line is found
		for (int i = 0; i < lines.size(); i++) {
			String s = lines.get(i).trim();
			if (!(s.isEmpty() || s.startsWith("#"))) {
				// this line is not blank, return the sublist starting at this line
				return lines.subList(i, lines.size());
			}
		}
		// at the end of file, return empty list
		return lines.subList(lines.size(), lines.size());
	}

	/**
	 * Attempts to read the width and height of the image from the file returning
	 * the remaining lines of the file.
	 * 
	 * @param lines the currently unread lines of text of the PPM file
	 * @return the remaining lines of text after reading the image width and height
	 * @throws PpmException          if the width or height is missing
	 * @throws NumberFormatException if a non-numeric width or height is found
	 */
	private List<String> readSize(List<String> lines) {
		if (lines.isEmpty()) {
			throw new PpmException("unexpected end of file");
		}
		// width and height should be on the first line of the sublist
		String s = lines.get(0).trim();
		String[] parts = s.split("\\s+");
		if (parts.length != 2) {
			throw new PpmException("missing size : " + s);
		}
		this.width = Integer.parseInt(parts[0]);
		this.height = Integer.parseInt(parts[1]);
		return lines.subList(1, lines.size());
	}

	/**
	 * Attempts to read the maximum color value from the file returning the
	 * remaining lines of the file.
	 * 
	 * @param lines the currently unread lines of text of the PPM file
	 * @return the remaining lines of text after reading the maximum color value
	 * @throws PpmException          if the maximum color value is missing
	 * @throws NumberFormatException if a non-numeric maximum color value is found
	 */
	private List<String> readMaxValue(List<String> lines) {
		if (lines.isEmpty()) {
			throw new PpmException("unexpected end of file");
		}
		// max color value should be on the first line of the sublist
		String s = lines.get(0).trim();
		String[] parts = s.split("\\s+");
		if (parts.length != 1) {
			throw new PpmException("missing max value : " + s);
		}
		this.maxValue = Integer.parseInt(parts[0]);
		return lines.subList(1, lines.size());
	}

	/**
	 * Tests that the specified value is between 0 and the maximum color value.
	 * 
	 * @param val a color value to test
	 * @throws PpmException if the specified value is not between 0 and the maximum
	 *                      color value
	 */
	private void testColorValue(int val) {
		if (val < 0) {
			throw new PpmException("color value less than zero");
		}
		if (val > this.maxValue) {
			throw new PpmException("color value greater than " + this.maxValue);
		}
	}

	/**
	 * Attempts to read the pixel color data from the remaining lines of the file.
	 * This method assumes that there are a multiple of 3 integer values on each
	 * line (i.e., RGB triplets are not split across multiple lines).
	 * 
	 * <p>
	 * The pixels are stored in the SimpleImage object this.img
	 * 
	 * @param lines the currently unread lines of text of the PPM file
	 * @throws PpmException          if a color value less than 0 or greater than
	 *                               the maximum color values is found
	 * @throws NumberFormatException if a non-numeric color value is found
	 */
	private void readPixels(List<String> lines) {
		
		List<Color> colorList = new ArrayList<>();
		String[] parts;
		for (int i = 0; i < lines.size(); i++) {
			
			parts = lines.get(i).trim().split("\\s+");
			for (int j = 0; j < parts.length; j+=3) {
				
				int red = Integer.parseInt(parts[j]);
				int green = Integer.parseInt(parts[j + 1]);
				int blue = Integer.parseInt(parts[j + 2]);
				
				if (red < 0 || green < 0 || blue < 0 || red > this.maxValue() || green > this.maxValue() || blue > this.maxValue()) {
					
					throw new PpmException("color value is < 0");
				}
				
				Color color = new Color(red, green, blue);
				colorList.add(color);
			}
		}
		
		for (int i = 0; i < this.height; i++) {
			for (int j = 0; j < this.width; j++) {
				
				this.img.set(i, j, colorList.get(i * width + j));
			}
		}
	}

	/**
	 * Returns the width of the image read by this reader.
	 * 
	 * @return the width of the image read by this reader
	 */
	public int width() {
		return this.width;
	}

	/**
	 * Returns the height of the image read by this reader.
	 * 
	 * @return the height of the image read by this reader
	 */
	public int height() {
		return this.height;
	}

	/**
	 * Returns the magic number of the image read by this reader.
	 * 
	 * @return the magic number of the image read by this reader
	 */
	public String magicNumber() {
		return this.magicNumber;
	}

	/**
	 * Returns the maximum color value of the image read by this reader.
	 * 
	 * @return the maximum color value of the image read by this reader
	 */
	public int maxValue() {
		return this.maxValue;
	}

	/**
	 * Returns the image read by this reader.
	 * 
	 * @return the image read by this reader
	 */
	public SimpleImage image() {
		return this.img;
	}

	/**
	 * Reads a small PPM image of the Queen's tricolor flag and displays the image.
	 * 
	 * @param args not used
	 */
	public static void main(String[] args) {
		// String filename = "tricolor.ppm";
		
		// or an image of Grant Hall
		String filename = "grant_hall.ppm";
		
		
		PpmAsciiReader r = new PpmAsciiReader("", filename);
		System.out.println("header : " + r.magicNumber());
		System.out.println("width  : " + r.width());
		System.out.println("height : " + r.height());
		System.out.println("max    : " + r.maxValue());

		JFrame frame = new JFrame("PpmAsciiReader");
		frame.setMinimumSize(new Dimension(500, 100));
		frame.getContentPane().setLayout(new FlowLayout());
		BufferedImage buf = r.image().asBufferedImage();
		frame.getContentPane().add(new JLabel(new ImageIcon(buf)));
		frame.pack();
		frame.setVisible(true);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

	}
}
