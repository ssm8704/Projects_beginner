import java.awt.*;
import java.awt.event.*;

public class TicTacToe extends Frame {
    static char[][] l = {{' ', ' ', ' '}, {' ', ' ', ' '}, {' ', ' ', ' '}};
    static int x, y;
    static char c = 'X';
    static String msg = "Player " + c + "'s turn";
    

    public TicTacToe() {
        addWindowListener(new WindowAdapter() {
            public void windowClosing(WindowEvent e) {
                System.exit(0);
            }
        });
        addMouseListener(new MouseAdapter() {
            public void mouseClicked(MouseEvent me) {
                
                repaint();
                int mouseX = me.getX();
                int mouseY = me.getY();
                int cellX = mouseX / (getWidth() / 3);
                int cellY = mouseY / (100);
                if (cellX >= 0 && cellX < 3 && cellY >= 0 && cellY < 3 && l[cellY][cellX] == ' ') {
                    l[cellY][cellX] = c;
                    if (wincase(c) == 1) {
                        msg = "Player " + c + " Won!!!";
                        repaint();
                        removeMouseListener(this);
                        return;
                    } else if (drawcase() == 1) {
                        msg = "Match Draw!!!";
                        repaint();
                        removeMouseListener(this);
                        return;
                    }
                    c = (c == 'X') ? 'O' : 'X';
                    msg="Player "+ c + "'s turn";
                    
                }
            }
        });
    }

    public static void main(String[] args) {
        TicTacToe tt = new TicTacToe();
        tt.setSize(new Dimension(300, 400));
        tt.setTitle("Tic Tac Toe");
        tt.setVisible(true);
    }

    public static int wincase(char a) {
        if (l[0][0] == a && l[1][1] == a && l[2][2] == a) return 1;
        if (l[0][2] == a && l[1][1] == a && l[2][0] == a) return 1;
        for (int i = 0; i < 3; i++) {
            if (l[i][0] == a && l[i][1] == a && l[i][2] == a) return 1;
            if (l[0][i] == a && l[1][i] == a && l[2][i] == a) return 1;
        }
        return 0;
    }

    public static int drawcase() {
        for (int i = 0; i < 3; i++)
            for (int j = 0; j < 3; j++)
                if (l[i][j] == ' ') return 0;
        return 1;
    }

    public void paint(Graphics g) {
        g.drawLine(100, 0, 100, 300);
        g.drawLine(200, 0, 200, 300);
        g.drawLine(0, 120, 300, 120);
        g.drawLine(0, 220, 300, 220);
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                String x = "" + l[i][j];
                g.drawString(x, j * 100 + 50, i * 100 + 50);
            }
        }
        g.drawString(msg, 90, 350);
    }
}
