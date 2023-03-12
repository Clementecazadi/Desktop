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
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int row = 0; row < height; row++)
    {
        for (int colun = 0; colun < width; colun++)
        {
            int sepiaRed = round(.393 * image[row][colun].rgbtRed + .769 * image[row][colun].rgbtGreen + .189 * image[row][colun].rgbtBlue);
            int sepiaGreen = round(.349 * image[row][colun].rgbtRed + .686 * image[row][colun].rgbtGreen + .168 * image[row][colun].rgbtBlue);
            int sepiaBlue = round(.272 * image[row][colun].rgbtRed + .534 * image[row][colun].rgbtGreen + .131 * image[row][colun].rgbtBlue);
            if (sepiaBlue > 255) sepiaBlue = 255;
            if (sepiaGreen > 255) sepiaGreen = 255;
            if (sepiaRed > 255) sepiaRed = 255;
            image[row][colun].rgbtBlue = sepiaBlue;
            image[row][colun].rgbtGreen = sepiaGreen;
            image[row][colun].rgbtRed = sepiaRed;
        }
    }
    return;
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
