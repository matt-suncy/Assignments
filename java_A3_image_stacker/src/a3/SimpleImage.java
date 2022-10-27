package a3;

import java.awt.Color;
import java.awt.Dimension;
import java.awt.FlowLayout;
import java.awt.image.BufferedImage;
import java.util.Arrays;

import javax.swing.ImageIcon;
import javax.swing.JFrame;
import javax.swing.JLabel;


/**
 * A simple representation of a color 2D image that allows the user to query the
 * dimensions of the image, retrieve an image pixel, and set an image pixel.
 * 
 * <p>
 * An image has a size defined by a positive integer width (in pixels) and positive
 * integer height (in pixels). 
 * 
 * <p>
 * Pixels are retrieved and set using 0-based row and column indexes. The upper-left
 * corner is the origin of the image (row = 0, column = 0).
 *
 */
public class SimpleImage {

	/*
	 * ADD THE FIELDS OF THE CLASS HERE
	 */
	private int height;
	
	private int width;
	
	private Color[][] colorImage;
	
	
	
	/**
	 * Initialize an image to the specified width and height. The pixels of the
	 * image are set to {@code Color.BLACK}.
	 * 
	 * @param width  the width of the image
	 * @param height the height of the image
	 * @throws IllegalArgumentException if the width or height of the image is less
	 *                                  than 1
	 */
	public SimpleImage(int width, int height) {
		
		if (width >= 1 && height >= 1) {
			this.width = width;
			this.height = height;
			this.colorImage = new Color[height][width];
			
			// nested for loop to set all elements to Color
			for (int i = 0; i < this.height; i++) {
				for (int j = 0; j < this.width; j++) {
					this.colorImage[i][j] = Color.black;
				}
			}
		}
		
		else {
			throw new IllegalArgumentException("height and width must be >= 1");
		}
	}

	/**
	 * Initialize an image by copying the specified image. The image has the
	 * same width and height of the copied image. The image has its own grid
	 * of pixels, and each pixel is equal to the corresponding pixel in the
	 * copied image.
	 * 
	 * @param img an image to copy
	 */
	public SimpleImage(SimpleImage img) {
		
		this.width = img.width;
		this.height = img.height;
		this.colorImage = img.colorImage;
	}

	public Color get(int row, int col) {
		
		if (row < 0 || row > this.height - 1) {
			throw new IndexOutOfBoundsException(row + " : row index out of range");
		}
		if (col < 0 || col > this.width - 1) {
			throw new IndexOutOfBoundsException(col + " : col index out of range");
		}
		
		return this.colorImage[row][col];
	}
	
	public int height() {
		
		return this.height;
	}
	
	public int width() {
		
		return this.width;
	}
	
	public void set(int row, int col, Color c) {
		
		if (row < 0 || row > this.height - 1) {
			throw new IndexOutOfBoundsException(row + " : row index out of range");
		}
		if (col < 0 || col > this.width - 1) {
			throw new IndexOutOfBoundsException(col + " : col index out of range");
		}
		
		this.colorImage[row][col] = c;
	}
	

	/**
	 * IMPLEMENTED FOR YOU.
	 * 
	 * <p>
	 * Returns a {@code BufferedImage} having equal pixels as this image. This
	 * method can be used to provide a suitable image for the Java Standard
	 * Library classes that are part of the Abstract Window Toolkit.
	 * 
	 * @return a BufferedImage having equal pixels as this image
	 */
	public BufferedImage asBufferedImage() {
		
		BufferedImage b = new BufferedImage(this.width(), this.height(), BufferedImage.TYPE_INT_ARGB);
		for (int i = 0; i < this.height(); i++) {
			for (int j = 0; j < this.width(); j++) {
				b.setRGB(j, i, this.get(i, j).getRGB());
			}
		}
		return b;
	}
	
	/**
	 * Creates and displays a SimpleImage.
	 * 
	 * @param args not used
	 */
	public static void main(String[] args) {
		SimpleImage img = new SimpleImage(100, 50);
		
		JFrame frame = new JFrame("SimpleImage");
		frame.setMinimumSize(new Dimension(500, 100));
		frame.getContentPane().setLayout(new FlowLayout());
		BufferedImage buf = img.asBufferedImage();
		frame.getContentPane().add(new JLabel(new ImageIcon(buf)));
		frame.pack();
		frame.setVisible(true);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	}
}
