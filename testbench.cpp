#include <ap_fixed.h>
#include <ap_int.h>
#include <cassert>
#include <iostream>

#include <hls_opencv.h>

typedef ap_uint<8> pixel_type;
typedef ap_int<8> pixel_type_s;
typedef ap_uint<96> u96b;
typedef ap_uint<32> word_32;
typedef ap_ufixed<8,0, AP_RND, AP_SAT> comp_type;
typedef ap_fixed<10,2, AP_RND, AP_SAT> coeff_type;

struct pixel_data {
	pixel_type blue;
	pixel_type green;
	pixel_type red;
};


void template_filter(volatile uint32_t* in_data, volatile uint32_t* out_data, unsigned short int* cookieX, unsigned short int* cookieY, unsigned short int* cookieWidth, unsigned short int* elmoX, unsigned short int* elmoY, unsigned short int* elmoWidth);


int main() {

	//Specify Input Image Absolute Path
	cv::Mat src_hls = cv::imread("/home/nb2618/project/Project_Part2/elmo.jpg", CV_LOAD_IMAGE_UNCHANGED);
	std::cout << "Image type: " << src_hls.type() << ", no. of channels: " << src_hls.channels() << std::endl;
	//src_hls.convertTo(src_hls, CV_8UC3);
	//cv::cvtColor(src_hls, src_hls, CV_BGR2RGBA);


	std::cout<<"SIZE  "<<src_hls.size()<<std::endl;
	uchar *data_p = src_hls.data;

	//Make sure that these match input image resolution
	int w = 1920;
	int h = 1080;


	uchar *image = (uchar *)malloc(w*h*4);
	unsigned short int cookieX = 0;
	unsigned short int cookieY = 0;
	unsigned short int cookieWidth = 0;
	unsigned short int elmoX = 0;
	unsigned short int elmoY = 0;
	unsigned short int elmoWidth = 0;

	for (int i=0; i<w*h; i++){
		image[4*i + 0] = data_p[3*i + 2]; //R - R
		image[4*i + 1] = data_p[3*i + 1]; // B - B
		image[4*i + 2] = data_p[3*i + 0]; // G - G
		image[4*i + 3] = 0;
	}

	template_filter((volatile uint32_t *)image, (volatile uint32_t *)image, &cookieX, &cookieY, &cookieWidth, &elmoX, &elmoY, &elmoWidth);

	//template_filter((volatile uint32_t *)image, (volatile uint32_t *)image);

	for (int i=0; i<w*h; i++){
		data_p[3*i + 2] = image[4*i + 0];
		data_p[3*i + 1] = image[4*i + 1];
		data_p[3*i + 0] = image[4*i + 2];
	}

	std::cout << "Cookie x: " << cookieX << "Cookie y: " << cookieY << "Cookie w: " << cookieWidth << std::endl;
	std::cout << "Elmo x: " << elmoX << "elmo y: " << elmoY << "elmo w: " << elmoWidth << std::endl;


	//Specify an Absolute Path for Storing Output Image
	cv::imwrite("/home/nb2618/project/Project_Part2/elmonew.jpg",src_hls);

	free(image);

	return 0;

}
