import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# Hàm câu 1 làm sáng 1 bức ảnh
def lighterImage(matrixImageOrigin):
    # Lấy ma trận gốc cộng với 1 hằng số ở đây là 40
    # Tuy nhiên phải lưu ý vì matrixImage có giới hạn tới 255 thôi
    # Nếu vượt quá 255 nó sẽ về 0 và cộng lên tiếp
    # Nên ta phải đổi miền giá trị lên thành uint32 để có thể cộng vượt quá 255
    matrixImage1=np.add(matrixImageOrigin,40,dtype=np.uint32)

    # Set miền giá trị của ma trận điểm ảnh trong khoảng từ 0 đến 255
    matrixImage1[matrixImage1>255]=255
    matrixImage1[matrixImage1<0]=0

    plt.imshow(matrixImage1.astype('uint8'))
    plt.show()
    # Chuyển ma trận về dạng PIL image tuy nhiên phải nhớ do ta đã
    # đổi miền giá trị thành uint32 nên muốn thành PIL phải cast về lại unint8
    image1=Image.fromarray(matrixImage1.astype('uint8'),'RGB')
    # Save image xuống máy
    image1.save("image1.jpg")



# Hàm câu 2 tương phản 1 bức ảnh
def contrastImage(matrixImageOrigin):
    # Lấy ma trận gốc nhân với 1 hằng số , ở đây là số 2, tuy nhiên do giới hạn của np.array
    # khi đọc ma trận từ ảnh chỉ có max tối đa là 255. Nên ta phải chuyển nó về dạng float64
    # Mục đích của việc chuyển về dạng float64 để khi nhân với 1 số thực nó sẽ ra số thực
    matrixImage2=np.multiply(matrixImageOrigin,2,dtype=np.float64)

    # Đặt miền giá trị cho tất cả phần tử ma trận trong [0,255]. Nếu có phần tử <0 ta cho =0
    # Nếu có phần tử >255 ta cho giá trị =255
    matrixImage2[matrixImage2<0]=0
    matrixImage2[matrixImage2>255]=255


    plt.imshow(matrixImage2.astype('uint8'))
    plt.show()

    # Chuyển ma trận về dạng PIL image tuy nhiên phải nhớ do ta đã
    # đổi miền giá trị thành float64 nên muốn thành PIL phải cast lại về lại uint8
    image2=Image.fromarray(matrixImage2.astype('uint8'),'RGB')
    # Save image xuống máy
    image2.save('image2.jpg')



# Hàm câu 3 chuyển đổi RGB thành ảnh xám
def convertToGrayscale(matrixImageOrigin):
    # Chuyển thành dạng số thực để nhân cho dễ
    matrixImage3=matrixImageOrigin.astype(np.float64)

    # Làm mờ ảnh cách 1: Tất cả các phần tử trong mảng ảnh có giá trị = (0.3 *R + 0.59*G + 0.11*B)
    # Duyệt từng dòng của ma trận
    for i in range (len(matrixImage3)):
        # Trong từng dòng lại có các cột 
        for j in range(len(matrixImage3[0])):
            # Tạo biến value = (0.3 *R + 0.59*G + 0.11*B)
            value=0
            # Mỗi phần tử của dòng gồm 3 thành phần RGB
            for k in range(0,3):
                # nếu là màu đỏ thì giá trị đỏ chiếm 0.3
                if(k==0):
                    matrixImage3[i][j][k]=float(matrixImage3[i][j][k])*0.3
                    value=value+matrixImage3[i][j][k]
                # nếu là màu green chiếm giá trị 0.59
                elif(k==1):
                    matrixImage3[i][j][k]=float(matrixImage3[i][j][k])*0.59
                    value=value+matrixImage3[i][j][k]
                # Blue chiếm 0.11
                else:
                    matrixImage3[i][j][k]=float(matrixImage3[i][j][k])*0.11
                    value=value+matrixImage3[i][j][k]
             # Sau khi tính giá trị cho kênh màu RGB của 1 phần tử trong ma trận
             # Duyệt qua RGB của phần tử đó và gán cho nó giá trị value
            for l in range(0,3):
                matrixImage3[i][j][l]=value
    return matrixImage3


# Hàm câu 4 lật ảnh ngang dọc
# Lật dọc
def reverseRow(matrixImageOrigin):
    # Đổi dòng đầu tiên với dòng cuối và cứ tiếp tục
    matrixImageRow=matrixImageOrigin[::-1]

    plt.imshow(matrixImageRow.astype('uint8'))
    plt.show()
    # Chuyển ma trận về dạng PIL image tuy nhiên phải nhớ do ta đã
    # đổi miền giá trị thành float64 nên muốn thành PIL phải cast lại về lại uint8
    image4a=Image.fromarray(matrixImageRow.astype('uint8'),'RGB')
    # Save image xuống máy
    image4a.save("image4b.jpg")

# Lật ngang
def reverseColumn(matrixImageOrigin):
    # Đổi cột đầu tiên với cột cuối và cứ tiếp tục
    matrixImageColumn=matrixImageOrigin[:,::-1]

    plt.imshow(matrixImageColumn.astype('uint8'))
    plt.show()

    # Chuyển ma trận về dạng PIL image tuy nhiên phải nhớ do ta đã
    # đổi miền giá trị thành float64 nên muốn thành PIL phải cast lại về lại uint8
    image4b=Image.fromarray(matrixImageColumn.astype('uint8'),'RGB')
    # Save image xuống máy
    image4b.save("image4a.jpg")


# Hàm câu 5 cộng 2 ảnh xám
def sumImage(matrixGray1,matrixGray2):
    # Do công dụng trước của hàm chuyển ảnh xám nên ma trận ảnh xám ở dạng float
    # Ta phải cast về dạng uint32 để thuận tiện cho việc cộng với save xuống
    matrixGray1=matrixGray1.astype(np.uint32)
    matrixGray2=matrixGray2.astype(np.uint32)
    # Lấy 2 ma trận cộng với nhau
    # Tuy nhiên phải lưu ý vì matrixImage5 có giới hạn tới 255 thôi
    # Nếu vượt quá 255 nó sẽ về 0 và cộng lên tiếp
    # Nên ta phải đổi miền giá trị lên thành uint32 để có thể cộng vượt quá 255
    matrixImage5=np.add(matrixGray1,matrixGray2,dtype=np.uint32)

    # Set miền giá trị của ma trận điểm ảnh trong khoảng từ 0 đến 255
    matrixImage5[matrixImage5>255]=255
    matrixImage5[matrixImage5<0]=0

    plt.imshow(matrixImage5.astype('uint8'))
    plt.show()

    # Chuyển ma trận về dạng PIL image tuy nhiên phải nhớ do ta đã
    # đổi miền giá trị thành uint32 nên muốn thành PIL phải cast về lại unint8
    image5=Image.fromarray(matrixImage5.astype('uint8'),'RGB')
    # Save image xuống máy
    image5.save("image5.jpg")


def main():
    image=Image.open("lena.jpg")
    #image.save('image1.jpg')
    matrixImageOrigin=np.array(image)
    #print("Matrix origin: ",matrixImageOrigin)

    # Câu 1. Làm sáng ảnh
    lighterImage(matrixImageOrigin)

    # Câu 2. Làm tương phản ảnh
    contrastImage(matrixImageOrigin)

    # Câu3. Chuyển ảnh RBG thành ảnh xám và save xuống file.jpg
    matrixImage3=convertToGrayscale(matrixImageOrigin)

    plt.imshow(matrixImage3.astype('uint8'))
    plt.show()
    # Chuyển ma trận về dạng PIL image tuy nhiên phải nhớ do ta đã
    # đổi miền giá trị thành float64 nên muốn thành PIL phải cast lại về lại uint8
    image3=Image.fromarray(matrixImage3.astype('uint8'),'RGB')
    # Save image xuống máy
    image3.save("image3.jpg")

    # Câu 4. Lật ảnh ngang-dọc
    
    # Lật ảnh ngang
    reverseColumn(matrixImageOrigin)
    # Lật ảnh dọc
    reverseRow(matrixImageOrigin)

    # Câu 5. Chồng 2 ảnh xám lên
    # Mở ảnh Vietnam.jpg và load vào matrixIm1
    image5a=Image.open("Vietnam.jpg")
    matrixIm1=np.array(image5a)

    # Mở ảnh England.jpg và load vào matrixIm2
    image5b=Image.open("England.jpg")
    matrixIm2=np.array(image5b)

    matrixGray1=convertToGrayscale(matrixIm1)
    matrixGray2=convertToGrayscale(matrixIm2)

    sumImage(matrixGray1,matrixGray2)
    
    

main()