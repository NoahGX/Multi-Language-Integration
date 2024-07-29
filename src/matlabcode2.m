% Read output variable from file
c_output_variable = fileread('c_output.txt');
h_output_variable = fileread('haskell_output.txt');
p_output_variable = fileread('prolog_output.txt');

% Convert string to numeric array
c_numeric_array = str2num(c_output_variable);
h_numeric_array = str2num(h_output_variable);
p_numeric_array = str2num(p_output_variable);

% Convert numeric array to unsigned char
c_output_array = uint8(c_numeric_array);
h_output_array = uint8(h_numeric_array);
p_output_array = uint8(p_numeric_array);

% Reshape to original size
originalSize = [256, 256];
c_resized_matrix = reshape(c_output_array, originalSize);
h_resized_matrix = reshape(h_output_array, originalSize);
p_resized_matrix = reshape(p_output_array, originalSize);

% Read image file
original_image = imread('mickey.png');
% original_image = imread('pengbrew.png');

% Display resized matrices in grid and save as one image
figure();
subplot(2, 2, 1);
imshow(original_image);
title('Original Image');

subplot(2, 2, 2);
imshow(c_resized_matrix);
title('Black & White Image using C Program');

subplot(2, 2, 3);
imshow(h_resized_matrix);
title('Color Flipped Image using Haskell Program');

subplot(2, 2, 4);
imshow(p_resized_matrix);
title('Rotated Image using Prolog Program');

% Save entire figure
saveas(gcf, 'output_image.png');