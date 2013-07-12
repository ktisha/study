PImage img;
import android.view.GestureDetector;
GestureDetector mGestureDetector;

void setup() {
  size(displayWidth, displayHeight);
  background(255);
  img = loadImage("225.gif");
  strokeWeight(5);
  line(0, displayHeight/2, displayWidth, displayHeight/2);
}

void draw() {
  int img_height=(displayWidth/2)*img.height/img.width;
  image(img, 0, 0, displayWidth/2, img_height);
}


void mouseDragged()
{
  line(pmouseX,pmouseY,mouseX,mouseY);
}

boolean sketchFullScreen() {
  return true;
}
