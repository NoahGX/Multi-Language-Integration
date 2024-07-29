% Read grayscale image
img = imread('mickey.png');
% img = imread('pengbrew.png');

% Specify target size
targetSize = [256, 256];

% Resize the image
img = imresize(img, targetSize);

% Reshape image into 1D array
img_1d = reshape(img, 1, []);

% Write data to file
dlmwrite('input.txt', img_1d, 'delimiter', ' ');