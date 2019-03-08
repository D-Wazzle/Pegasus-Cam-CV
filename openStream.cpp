#include <iostream>
#include <string>

#include <opencv2/core.hpp>
#include <opencv2/videoio.hpp>

using namespace std;
using namespace cv;

int main(int argc, char *argv[])
{
        VideoCapture stream("http://192.168.50.20:3000/html/cam_pic_new.php?time=9999999999999&pDelay=40000");

	if(!stream.isOpened()){
		cout << "Could not open the stream!" << endl;
		return -1;
	}

	int ex = static_cast<int>(stream.get(CAP_PROP_FOURCC));
	char EXT[] = {(char)(ex & 0xFF), (char)((ex & 0xFF00) >> 8), (char)((ex & 0xFF0000) >> 16), (char)((ex & 0xFF000000) >> 24), 0};
	Size S = Size((int)stream.get(CAP_PROP_FRAME_WIDTH), (int)stream.get(CAP_PROP_FRAME_HEIGHT));

	VideoWriter outputVideo;
	outputVideo.open("stream.avi", ex, stream.get(CAP_PROP_FPS), S, true);

	if(!outputVideo.isOpened()){
		cout << "Could not open the output video!" << endl;
		return -1;
	}

	cout << "Input frame resolution: Width = " << S.width << ", Height = " << S.height << "of #: " << stream.get(CAP_PROP_FRAME_COUNT) << endl;
	cout << "Input codec type:" << EXT << endl;

	int channel = 2;
	Mat src, res;
	vector<Mat> spl;

	for(;;){
		stream >> src;
		if(src.empty()) break;

		split(src, spl);
		for(int i = 0; i < 3; ++i){
			if(i != channel)
				spl[i] = Mat::zeros(S, spl[0].type());
		}

		merge(spl, res);
		outputVideo << res;
	}

	cout << "Finsihed writing" << endl;

	return 0;
}
