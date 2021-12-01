from sklearn.svm import SVC,LinearSVC
from sklearn.model_selection import GridSearchCV, train_test_split,KFold
from sklearn.model_selection import KFold
from sklearn.metrics import roc_curve, auc,accuracy_score,classification_report
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import numpy as np
class ML:
    def __init__(self,data,label,trainFunction):
        self.data = data
        self.label = label
        self.trainFunction = trainFunction

    def kfoldML(self,foldNum=5):
        kfold = KFold(n_splits=foldNum,random_state=10086,shuffle=True)
        mean_tpr = 0.0              # 用来记录画平均ROC曲线的信息
        mean_fpr = np.linspace(0, 1, 100)
        cnt = 0
        #plt.figure(figsize=(8,8))
        accs  =[]
        fig ,ax = plt.subplots()
        i = 0
        for train_index,test_index in kfold.split(self.data):
            x_train,x_test,=self.data[train_index],self.data[test_index]
            y_train,y_test=self.label[train_index],self.label[test_index]
            cnt += 1
            fpr,tpr,roc_auc,acc = self.trainFunction(x_train,y_train,x_test,y_test)
            mean_tpr += np.interp(mean_fpr, fpr, tpr)   # 插值函数 interp(x坐标,每次x增加距离,y坐标)  累计每次循环的总值后面求平均值
            mean_tpr[0] = 0.0 
            accs.append(acc)
            ax.plot(fpr, tpr,
                lw=2, label='ROC(area = %0.2f)(fold %d)' % (roc_auc,i+1)) ###假正率为横坐标，真正率为纵坐标做曲线
            i+=1
        ax.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
        mean_tpr /= cnt   # 求数组的平均值
        mean_tpr[-1] = 1.0   # 坐标最后一个点为（1,1）  以1为终点
        mean_auc = auc(mean_fpr, mean_tpr)
        ax.plot(mean_fpr, mean_tpr, 'k--',label='Mean ROC (area = %.2f)'% (mean_auc), lw=2)
        ax.set(ylabel='True Positive Rate',xlabel='False Positive Rate')
        #plt.title('The receiver operating characteristic curves (ROC) and \n area under ROCs (AUC) of leave-one-center cross-validations')
        ax.legend(loc="lower right")
        print('平均准确率为：',np.mean(accs))  
    
def svmTrainTest(x_train,y_train,x_test,y_test,clf=SVC()):
    y_test = y_test.astype(np.int8)
    y_train = y_train.astype(np.int8)
    svc = clf
    c_range = np.logspace(-5, 5, 30, base=2)
    gamma_range = np.logspace(-9, 3, 30, base=2)
    param_grid = [{'kernel': ['linear'], 'C': c_range, 'gamma': gamma_range}]
    grid = GridSearchCV(svc, param_grid, cv=5, n_jobs=-1)
    y_score = grid.fit(x_train, y_train).decision_function(x_test)
    y_hat = grid.predict(x_test)
    acc = accuracy_score(y_test, y_hat)
    print(classification_report(y_test,y_hat))
    #acc = grid.score(x_test, y_test)
    fpr,tpr,threshold = roc_curve(y_test, y_score) ###计算真正率和假正率
    roc_auc = auc(fpr,tpr) ###计算auc的值
    return fpr,tpr,roc_auc,acc

