package a3;

import java.awt.FlowLayout;
import java.awt.image.BufferedImage;
import javax.swing.ImageIcon;
import javax.swing.JFrame;
import javax.swing.JLabel;


/**
 * Image noise reduction program via image stacking.
 * 
 * <p>
 * Uncomment one pair of dir/prefix lines to denoise different series of images.
 * The images are located in the img folder of the project.
 *
 */
public class Denoise {

	/**
	 * Entry point of the program.
	 * 
	 * @param args not used
	 */
	public static void main(String[] args) {
		// cone nebula
		String dir = "1";
		String prefix = "cone_nebula";
		
		// N44F
		//String dir = "2";
		//String prefix = "n44f";
		
		// Orion nebula
		//String dir = "3";
		//String prefix = "orion";
		
		// Carina nebula
		//String dir = "4";
		//String prefix = "wfc3_uvis";
		
		int n = 10;
		PpmStacker stacker = new PpmStacker(dir, prefix, n);
		
		JFrame frame = new JFrame();
		frame.getContentPane().setLayout(new FlowLayout());
		BufferedImage buf = stacker.getAverage().asBufferedImage();
		frame.getContentPane().add(new JLabel(new ImageIcon(buf)));
		frame.pack();
		frame.setVisible(true);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	}

}
