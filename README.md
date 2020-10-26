# Table of Content
- [Table of Content](#table-of-content)
  - [項目說明](#項目說明)
  - [目錄結構](#目錄結構)
  - [Table Schema](#table-schema)
    - [Aliyun CDN關係數據表](#aliyun-cdn關係數據表)
    - [Aliyun WAF關係數據表](#aliyun-waf關係數據表)
    - [Aliyun WAF Whitelist白名單列表](#aliyun-waf-whitelist白名單列表)

## 項目說明
- 作業系統：`CentOS 7`
- 語言：`Python 3.6` + `Javascript(JQuery)`
- 前端：`AdminLTE 2 前端模板`
- 後端框架：`Django` + `Django REST Framework`+ `Django REST Framework JWT`

## 目錄結構
* `assets`: 資產管理Django APP。
* `scripts`: 腳本放置目錄。
* `static`: 靜態資源放置位置 , 如CSS、JS等文件。
* `templates`: 基底模板放置位置 , 其他模板會繼承基底模板。****
* `login`: 登入模塊 , 使用內建Django的用戶模型 , 使用REST_FRAMEWORK 的 JWT方式驗證API請求





## Table Schema
### Aliyun CDN關係數據表

```SQL
SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for cdn
-- ----------------------------
DROP TABLE IF EXISTS `cdn`;
CREATE TABLE `cdn` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'id',
  `Product_ID` varchar(10) DEFAULT NULL COMMENT '產品ID',
  `Domain_Name` varchar(50) NOT NULL COMMENT '配置的CDN域名',
  `SSL_Protocol` varchar(5) NOT NULL COMMENT '是否啟用Https',
  `CDN_Type` varchar(14) NOT NULL COMMENT 'CDN類型 : download , web , video',
  `Cname` varchar(255) NOT NULL COMMENT '阿里生成的Cname',
  `Source_Type` varchar(255) NOT NULL COMMENT '回源類型 : OSS、IP、Domain',
  `Source_Content` varchar(255) NOT NULL COMMENT '回源內容',
  `Domain_Status` varchar(10) NOT NULL COMMENT '該域名是否正在使用CDN',
  `Belong_Account` varchar(30) NOT NULL COMMENT '屬於哪個阿里帳號',
  `Region` varchar(40) DEFAULT NULL COMMENT '所屬地區',
  `Service_Name` varchar(40) NOT NULL COMMENT '模塊名稱',
  `Purpose` varchar(100) DEFAULT NULL COMMENT '用途說明',
  `Update_Time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '該筆數據被更新時間',
  `is_delete` tinyint(1) NOT NULL DEFAULT '0' COMMENT '邏輯刪除',
  PRIMARY KEY (`id`,`Domain_Name`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=147 DEFAULT CHARSET=utf8;

SET FOREIGN_KEY_CHECKS = 1;
```

### Aliyun WAF關係數據表

```SQL
SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for waf
-- ----------------------------
DROP TABLE IF EXISTS `waf`;
CREATE TABLE `waf` (
  `Domain_Name` varchar(40) NOT NULL COMMENT '配置WAF的域名',
  `Instance_ID` varchar(30) NOT NULL COMMENT 'WAF實例ID',
  `Source_IP_Addr` varchar(255) DEFAULT '' COMMENT '回源IP , 使用逗號組合IP',
  `Region` varchar(255) DEFAULT NULL COMMENT 'WAF服務區域',
  `Belong_Account` varchar(30) NOT NULL COMMENT '屬於哪個阿里帳號下',
  `Update_Time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '該筆數據更新時間',
  `is_delete` tinyint(1) NOT NULL DEFAULT '0' COMMENT '邏輯刪除',
  `is_update` tinyint(1) NOT NULL DEFAULT '1' COMMENT '是否更新回源IP欄位 , 欄位默認成功 , 當同步數據失敗時修改為失敗(0)',
  PRIMARY KEY (`Domain_Name`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

SET FOREIGN_KEY_CHECKS = 1;
```

### Aliyun WAF Whitelist白名單列表
```SQL
SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for waf_whitelist
-- ----------------------------
DROP TABLE IF EXISTS `waf_whitelist`;
CREATE TABLE `waf_whitelist` (
  `Domain_Name` varchar(50) NOT NULL COMMENT 'WAF內配置的網站域名',
  `IP_Address` varchar(15) NOT NULL COMMENT '白名單IP',
  `is_delete` tinyint(1) NOT NULL DEFAULT '0' COMMENT '邏輯刪除',
  `Update_Time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '該筆數據更新時間',
  `Acl_ID` varchar(15) NOT NULL,
  `Acl_Name` varchar(50) NOT NULL,
  PRIMARY KEY (`Domain_Name`,`IP_Address`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

SET FOREIGN_KEY_CHECKS = 1;

```