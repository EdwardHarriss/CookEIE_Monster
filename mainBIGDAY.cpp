#include <ap_fixed.h>
#include <ap_int.h>
#include <stdint.h>
#include <assert.h>

//typedef ap_uint<24> pixel_type;
typedef unsigned char pixel_type;
typedef ap_int<8> pixel_type_s;
typedef ap_uint<96> u96b;
typedef ap_uint<32> word_32;
typedef unsigned short int dimensions;
/*
struct pixel_data {
pixel_type blue;
pixel_type green;
pixel_type red;
};

struct puppet {
bool start;
dimensions x;
dimensions y;
dimensions width;
};
*/

void template_filter(volatile uint32_t* in_data, volatile uint32_t* out_data, dimensions* cookieX,dimensions* cookieY, dimensions* cookieWidth, dimensions* elmoX,dimensions* elmoY, dimensions* elmoWidth){
	#pragma HLS INTERFACE s_axilite port=return

	#pragma HLS INTERFACE m_axi depth=2073600 port=in_data offset=slave
	#pragma HLS INTERFACE m_axi depth=2073600 port=out_data offset=slave
	#pragma HLS INTERFACE s_axilite port=cookieX
	#pragma HLS INTERFACE s_axilite port=cookieY
	#pragma HLS INTERFACE s_axilite port=cookieWidth
	#pragma HLS INTERFACE s_axilite port=elmoX
	#pragma HLS INTERFACE s_axilite port=elmoY
	#pragma HLS INTERFACE s_axilite port=elmoWidth




	pixel_type in_red;
	pixel_type in_green;
	pixel_type in_blue;

	pixel_type out_red;
	pixel_type out_green;
	pixel_type out_blue;

	pixel_type prev_green;
	pixel_type prev_red;
	pixel_type prev_blue;


	bool cookieStart;

	bool elmoStart;
	dimensions h = 1080;
	dimensions w = 1920;

	for (dimensions y = 0; y < h; ++y) {

		unsigned short int counter = 0;
		cookieStart = false;
		elmoStart = false;

		for (dimensions x = 0; x < w; ++x) {

			#pragma HLS PIPELINE II=1
			#pragma HLS LOOP_FLATTEN off

			unsigned int current = *in_data++;

			in_red = current & 0xFF;
			in_green = (current >> 8) & 0xFF;
			in_blue = (current >> 16) & 0xFF;


			out_red = in_red;
			out_blue = in_blue;
			out_green = in_green;


			if (x % 25 == 0){ //change .widths as well

				if(cookieStart) {

					if(in_blue>100 && (in_blue - in_red )>80 && (in_blue - in_red )<150 && (in_blue - in_green )<62 && (in_blue - in_green )>35 && prev_blue<40 && prev_red<40 && prev_green<40) {
						if(counter > *cookieWidth) {
							*cookieWidth = counter * 25;
							*cookieX = x;
							*cookieY = y;

						}
					} else if(in_blue<40 && in_red<40 && in_green<40 && prev_blue<40 && prev_red<40 && prev_green<40) {
						counter++;
						out_red = 255;
						out_green = 255;
						out_blue = 255;
					} else { // this is same if statement as for elmo black; more efficient to write seperate function?
						cookieStart = false;
					}

				} else if(elmoStart) {

					if(in_red>135 && (in_red-in_blue)<155 && (in_red-in_blue)>80 && (in_red-in_green)<155 && (in_red-in_green)>80 && prev_blue<40 && prev_red<40 && prev_green<40) {
						if(counter > *elmoWidth) {
							*elmoWidth = counter * 25;
							*elmoX = x;
							*elmoY = y;
						}
					} else if(in_blue<40 && in_red<40 && in_green<40 && prev_blue<40 && prev_red<40 && prev_green<40) {
						counter++;
						out_red = 255;
						out_green = 255;
						out_blue = 255;

					} else {
						elmoStart = false;
					}

				} else {
					if(in_blue<40 && in_red<40 && in_green<40) {
						if(prev_blue>100 && (prev_blue-prev_red)>80 && (prev_blue-prev_red)<150 && (prev_blue-prev_green)<62 && (prev_blue-prev_green)>35) {
							cookieStart = true;
							counter = 0;
						} else if(prev_red > 135 && (prev_red-prev_blue)<155 && (prev_red-prev_blue)>80 && (prev_red-prev_green)<155 && (prev_red-prev_green)>80) {
							elmoStart = true;
							counter = 0;
						}
					}
				}


				prev_red = in_red;
				prev_green = in_green;
				prev_blue = in_blue;
			}

			unsigned int output = out_red | (out_green << 8) | (out_blue << 16);
			*out_data++ = output;
		}

	}

}
