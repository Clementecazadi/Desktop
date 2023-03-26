#include "helpers.h"
#include <stdio.h>
#include <math.h>
#define RED_COLOR 0
#define GREEN_COLOR 1
#define BLUE_COLOR 2
// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int average = round((image[i][j].rgbtBlue + image[i][j].rgbtGreen + image[i][j].rgbtRed) / 3.0);
            image[i][j].rgbtBlue = average;
            image[i][j].rgbtGreen = average;
            image[i][j].rgbtRed = average;
        }
    }
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        int k = width - 1;
        for(int j = 0; j < round(width/2); j++)
        {
            RGBTRIPLE tmp = image[i][j];
            image[i][j] = image[i][k];
            image[i][k] = tmp;
            k--;
        }
    }
    return;
}

// Blur image
int get_blur(int i, int j, int height, int width, RGBTRIPLE image[height][width], int color_p)
{
    float count = 0;
    int sum = 0;
    for (int row = i - 1; row <= i + 1; row++)
    {
        for (int colun = j - 1; colun <= j + 1; colun++)
        {
            if (row < 0 || row >= height || colun < 0 || colun >= width)
            {
                continue;
            }
            if (color_p == RED_COLOR)
            {
                sum += image[row][colun].rgbtRed;
            }
            else if (color_p == GREEN_COLOR)
            {
                sum += image[row][colun].rgbtGreen;
            }
            else
            {
                sum += image[row][colun].rgbtBlue;
            }
            count++;
        }
    }
    return round(sum / count);
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE copy[height][width];
    for (int row = 0; row < height; row++)
    {
        for (int colun = 0; colun < width; colun++)
        {
            copy[row][colun] = image[row][colun];
        }
    }

    for (int row = 0; row < height; row++)
    {
        for (int colun = 0; colun < width; colun++)
        {
            image[row][colun].rgbtRed = get_blur(row, colun, height, width, copy, RED_COLOR);
            image[row][colun].rgbtGreen = get_blur(row, colun, height, width, copy, GREEN_COLOR);
            image[row][colun].rgbtBlue = get_blur(row, colun, height, width, copy, BLUE_COLOR);
         }
    }
    return;
}
int get_edge(int i, int j, int height, int width, RGBTRIPLE image[height][width], int color_p)
{
    int gx[3][3] = {{-1, 0, 1}, {-2, 0, 2}, {-1, 0, 1}};
    int gy[3][3] = {{-1, -2, -1}, {0, 0, 0}, {1, 2, 1}};
    int blue_x = 0, green_x = 0, red_x = 0;
    int blue_y = 0, green_y = 0, red_y = 0;
    for (int row = i - 1, r = 0; row <= i + 1; row++, r++)
    {
        for (int colun = j - 1, c = 0; colun <= j + 1; colun++, c++)
        {
            if (row < 0 || row >= height || colun < 0 || colun >= width)
            {
                printf("%i--%i--%i--%i\n", r, c, row, colun);
                continue;
            }
            if (color_p == RED_COLOR)
            {
                red_x += gx[r][c] * image[row][colun].rgbtRed;
                red_y += gy[r][c] * image[row][colun].rgbtRed;
            }
            else if (color_p == GREEN_COLOR)
            {
                green_x += gx[r][c] * image[row][colun].rgbtGreen;
                green_y += gy[r][c] * image[row][colun].rgbtGreen;
            }
            else
            {
                blue_x += gx[r][c] * image[row][colun].rgbtBlue;
                blue_y += gy[r][c] * image[row][colun].rgbtBlue;
            }
        }
    }
    //printf("---------\n");
    if (color_p == RED_COLOR)
    {
        int red = round(sqrt(red_x * red_x + red_y * red_y));
        if (red > 255) red = 255;
        return red;
    }
    else if (color_p == GREEN_COLOR)
    {
        int green = round(sqrt(green_x * green_x + green_y * green_y));
        if (green > 255) green = 255;
        return green;
    }
    else
    {
        int blue = round(sqrt(blue_x * blue_x + blue_y * blue_y));
        if (blue > 255) blue = 255;
        return blue;
    }
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE copy[height][width];
    for (int row = 0; row < height; row++)
    {
        for (int colun = 0; colun < width; colun++)
        {
            copy[row][colun] = image[row][colun];
        }
    }
    for (int row = 0; row < height; row++)
    {
        for (int colun = 0; colun < width; colun++)
        {
            image[row][colun].rgbtBlue = get_edge(row, colun, height, width, copy, BLUE_COLOR);
            image[row][colun].rgbtGreen = get_edge(row, colun, height, width, copy, GREEN_COLOR);
            image[row][colun].rgbtRed = get_edge(row, colun, height, width, copy, RED_COLOR);
        }
    }
    return;
}