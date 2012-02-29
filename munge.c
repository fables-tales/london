#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    FILE* image_data = fopen("output_image", "r");
    fseek(image_data, 0L, SEEK_END);
    long numbytes = ftell(image_data);
    
    char* buffer = malloc(sizeof(char) * numbytes);
    fseek(image_data, 0L, SEEK_SET);
    fread(buffer, sizeof(char), numbytes, image_data);
    fclose(image_data);
    
    FILE* input_data = fopen("csv_data", "r");
    fseek(input_data, 0L, SEEK_END);
    numbytes = ftell(input_data);
    char* buffer2 = malloc(sizeof(char) * numbytes);
    fseek(input_data, 0L, SEEK_SET);
    fread(buffer2, sizeof(char), numbytes, image_data);
    fclose(image_data);

    

    int* radius = malloc(sizeof(int) * 1024);
    int* x = malloc(sizeof(int) * 1024);
    int* y = malloc(sizeof(int) * 1024);

    int linecount = 0;
    char* line = strtok(buffer2, "\n");
    while (line != NULL) {
        int a,b,c;

        sscanf(line, "%d %d %d", &a,&b,&c); 
        radius[linecount] = a;
        x[linecount] = b;
        y[linecount] = c;
        linecount++;
        line = strtok(NULL, "\n");
    }

    
    int width = 2668;
    int height = 1494; 
    int i,j,k;
    float* lightness_map = malloc(sizeof(float) * width * height);
    for (i = 0; i < height; i++) {
        for (j = 0; j < width; j++) {
            float lightness = 0.0f;
            for (k = 0; k < linecount; k++) {
                float dx = x[k] - j; 
                float dy = y[k] - i;
                float glow_radius = radius[k]/11.0;
                if (dx != 0 || dy != 0) {
                    if (dx * dx + dy * dy < 10000000000000.0f) {
                        float per = glow_radius/(abs(dx*dx)+abs(dy*dy)+300); 
                        lightness += per;
                    }
                }
            }
            if (lightness > 1.0f) lightness = 1.0f;
            if (lightness < 0.3f) lightness = 0.3f;
            lightness_map[i*width+j] = lightness;
        }
    }


    float lightness;
    for (i = 0; i < height; i++) {
        for (j = 0; j < width; j++) {
            lightness = lightness_map[i*width+j];
            unsigned char b,c;
            unsigned char a = buffer[4*(i*width+j)];
            a *= lightness;
            buffer[4*(i*width+j)] = a;

            b = buffer[4*(i*width+j)+1];
            b *= lightness;
            buffer[4*(i*width+j)+1] = b;

            c = buffer[4*(i*width+j)+2];
            c *= lightness;
            buffer[4*(i*width+j)+2] = c;
        }
    }

    FILE* out = fopen("output_pixel_data", "w");
    fwrite(buffer, sizeof(char), 4 * width * height, out);
    fclose(out);

    
}
