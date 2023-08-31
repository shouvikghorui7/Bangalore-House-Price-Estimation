{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import json\n",
    "import pandas as pd\n",
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt\n",
    "from datetime import datetime\n",
    "from sklearn.preprocessing import LabelEncoder"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>id</th>\n",
       "      <th>type</th>\n",
       "      <th>locality</th>\n",
       "      <th>activation_date</th>\n",
       "      <th>latitude</th>\n",
       "      <th>longitude</th>\n",
       "      <th>lease_type</th>\n",
       "      <th>gym</th>\n",
       "      <th>lift</th>\n",
       "      <th>swimming_pool</th>\n",
       "      <th>...</th>\n",
       "      <th>bathroom</th>\n",
       "      <th>facing</th>\n",
       "      <th>cup_board</th>\n",
       "      <th>floor</th>\n",
       "      <th>total_floor</th>\n",
       "      <th>amenities</th>\n",
       "      <th>water_supply</th>\n",
       "      <th>building_type</th>\n",
       "      <th>balconies</th>\n",
       "      <th>rent</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>10720</th>\n",
       "      <td>ff8081815cee9dbf015cef798b14214e</td>\n",
       "      <td>BHK3</td>\n",
       "      <td>Annapurneshwari Nagar</td>\n",
       "      <td>2018-10-01 21:57:00</td>\n",
       "      <td>12.977327</td>\n",
       "      <td>77.501541</td>\n",
       "      <td>ANYONE</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>...</td>\n",
       "      <td>3.0</td>\n",
       "      <td>E</td>\n",
       "      <td>3.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>{\"LIFT\":false,\"GYM\":false,\"INTERNET\":true,\"AC\"...</td>\n",
       "      <td>CORP_BORE</td>\n",
       "      <td>IF</td>\n",
       "      <td>5.0</td>\n",
       "      <td>17000.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10244</th>\n",
       "      <td>ff80818162e6a3300162f0efd8276384</td>\n",
       "      <td>BHK2</td>\n",
       "      <td>Sangeeta Topaz, Hoodi, Bengaluru, Karnataka, I...</td>\n",
       "      <td>23-04-2018 14:02</td>\n",
       "      <td>12.989211</td>\n",
       "      <td>77.715397</td>\n",
       "      <td>FAMILY</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>...</td>\n",
       "      <td>2.0</td>\n",
       "      <td>N</td>\n",
       "      <td>7.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>{\"SC\":true,\"INTERCOM\":true,\"AC\":false,\"PB\":tru...</td>\n",
       "      <td>CORPORATION</td>\n",
       "      <td>AP</td>\n",
       "      <td>3.0</td>\n",
       "      <td>23000.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7326</th>\n",
       "      <td>ff80818153d5d5b70153e00a5cce0c4c</td>\n",
       "      <td>BHK2</td>\n",
       "      <td>Murugesh Pallya</td>\n",
       "      <td>2018-08-02 19:47:00</td>\n",
       "      <td>12.959188</td>\n",
       "      <td>77.656335</td>\n",
       "      <td>ANYONE</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>...</td>\n",
       "      <td>2.0</td>\n",
       "      <td>N</td>\n",
       "      <td>2.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>{\"LIFT\":false,\"GYM\":false,\"INTERNET\":true,\"AC\"...</td>\n",
       "      <td>CORP_BORE</td>\n",
       "      <td>IF</td>\n",
       "      <td>0.0</td>\n",
       "      <td>24000.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1436</th>\n",
       "      <td>ff808181641c39eb01641cbf32fe6b78</td>\n",
       "      <td>BHK2</td>\n",
       "      <td>Kaggadasapura</td>\n",
       "      <td>22-06-2018 11:09</td>\n",
       "      <td>12.976973</td>\n",
       "      <td>77.670153</td>\n",
       "      <td>ANYONE</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>...</td>\n",
       "      <td>1.0</td>\n",
       "      <td>E</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>{\"LIFT\":false,\"GYM\":false,\"INTERNET\":false,\"AC...</td>\n",
       "      <td>CORP_BORE</td>\n",
       "      <td>IF</td>\n",
       "      <td>0.0</td>\n",
       "      <td>13000.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2299</th>\n",
       "      <td>ff8081816035b49201604440a4536d0c</td>\n",
       "      <td>BHK2</td>\n",
       "      <td>Koramangala</td>\n",
       "      <td>2017-11-12 16:04:00</td>\n",
       "      <td>12.934838</td>\n",
       "      <td>77.612270</td>\n",
       "      <td>FAMILY</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>...</td>\n",
       "      <td>2.0</td>\n",
       "      <td>E</td>\n",
       "      <td>2.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>7.0</td>\n",
       "      <td>{\"LIFT\":true,\"GYM\":true,\"INTERNET\":true,\"AC\":t...</td>\n",
       "      <td>CORP_BORE</td>\n",
       "      <td>AP</td>\n",
       "      <td>0.0</td>\n",
       "      <td>35000.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18569</th>\n",
       "      <td>ff808181630c64f00163108121861e3e</td>\n",
       "      <td>BHK2</td>\n",
       "      <td>Panathur</td>\n",
       "      <td>29-04-2018 15:47</td>\n",
       "      <td>12.934903</td>\n",
       "      <td>77.702967</td>\n",
       "      <td>FAMILY</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>...</td>\n",
       "      <td>2.0</td>\n",
       "      <td>E</td>\n",
       "      <td>6.0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>5.0</td>\n",
       "      <td>{\"LIFT\":true,\"GYM\":false,\"INTERNET\":true,\"AC\":...</td>\n",
       "      <td>BOREWELL</td>\n",
       "      <td>AP</td>\n",
       "      <td>2.0</td>\n",
       "      <td>25000.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4541</th>\n",
       "      <td>ff808181592254fb0159252d951f24ff</td>\n",
       "      <td>BHK3</td>\n",
       "      <td>Ejipura</td>\n",
       "      <td>16-06-2018 21:04</td>\n",
       "      <td>12.933155</td>\n",
       "      <td>77.636593</td>\n",
       "      <td>ANYONE</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>...</td>\n",
       "      <td>3.0</td>\n",
       "      <td>SW</td>\n",
       "      <td>3.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>{\"LIFT\":true,\"GYM\":false,\"INTERNET\":true,\"AC\":...</td>\n",
       "      <td>CORP_BORE</td>\n",
       "      <td>IF</td>\n",
       "      <td>3.0</td>\n",
       "      <td>38000.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18370</th>\n",
       "      <td>ff808181523600dd015236198a920101</td>\n",
       "      <td>RK1</td>\n",
       "      <td>Marathahalli</td>\n",
       "      <td>2018-09-02 15:24:00</td>\n",
       "      <td>12.950288</td>\n",
       "      <td>77.699063</td>\n",
       "      <td>ANYONE</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>...</td>\n",
       "      <td>1.0</td>\n",
       "      <td>E</td>\n",
       "      <td>0.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>{\"LIFT\":false,\"GYM\":false,\"INTERNET\":true,\"AC\"...</td>\n",
       "      <td>CORP_BORE</td>\n",
       "      <td>IF</td>\n",
       "      <td>0.0</td>\n",
       "      <td>8500.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13038</th>\n",
       "      <td>ff808181550b5f7b01550bcec08a0e03</td>\n",
       "      <td>BHK1</td>\n",
       "      <td>J P Nagar</td>\n",
       "      <td>2017-07-11 12:54:00</td>\n",
       "      <td>12.900169</td>\n",
       "      <td>77.585651</td>\n",
       "      <td>ANYONE</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>...</td>\n",
       "      <td>1.0</td>\n",
       "      <td>N</td>\n",
       "      <td>2.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>{\"LIFT\":false,\"GYM\":false,\"INTERNET\":true,\"AC\"...</td>\n",
       "      <td>CORP_BORE</td>\n",
       "      <td>IF</td>\n",
       "      <td>1.0</td>\n",
       "      <td>9500.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2859</th>\n",
       "      <td>ff8081815fcf9c0a015fd26cd4b74d3f</td>\n",
       "      <td>BHK3</td>\n",
       "      <td>Kumaraswamy Layout</td>\n",
       "      <td>19-11-2017 15:01</td>\n",
       "      <td>12.908354</td>\n",
       "      <td>77.561678</td>\n",
       "      <td>ANYONE</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>...</td>\n",
       "      <td>2.0</td>\n",
       "      <td>N</td>\n",
       "      <td>0.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>{\"LIFT\":false,\"GYM\":false,\"INTERNET\":true,\"AC\"...</td>\n",
       "      <td>CORP_BORE</td>\n",
       "      <td>IF</td>\n",
       "      <td>1.0</td>\n",
       "      <td>14000.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>10 rows × 25 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "                                     id  type  \\\n",
       "10720  ff8081815cee9dbf015cef798b14214e  BHK3   \n",
       "10244  ff80818162e6a3300162f0efd8276384  BHK2   \n",
       "7326   ff80818153d5d5b70153e00a5cce0c4c  BHK2   \n",
       "1436   ff808181641c39eb01641cbf32fe6b78  BHK2   \n",
       "2299   ff8081816035b49201604440a4536d0c  BHK2   \n",
       "18569  ff808181630c64f00163108121861e3e  BHK2   \n",
       "4541   ff808181592254fb0159252d951f24ff  BHK3   \n",
       "18370  ff808181523600dd015236198a920101   RK1   \n",
       "13038  ff808181550b5f7b01550bcec08a0e03  BHK1   \n",
       "2859   ff8081815fcf9c0a015fd26cd4b74d3f  BHK3   \n",
       "\n",
       "                                                locality      activation_date  \\\n",
       "10720                              Annapurneshwari Nagar  2018-10-01 21:57:00   \n",
       "10244  Sangeeta Topaz, Hoodi, Bengaluru, Karnataka, I...     23-04-2018 14:02   \n",
       "7326                                     Murugesh Pallya  2018-08-02 19:47:00   \n",
       "1436                                       Kaggadasapura     22-06-2018 11:09   \n",
       "2299                                         Koramangala  2017-11-12 16:04:00   \n",
       "18569                                           Panathur     29-04-2018 15:47   \n",
       "4541                                             Ejipura     16-06-2018 21:04   \n",
       "18370                                       Marathahalli  2018-09-02 15:24:00   \n",
       "13038                                          J P Nagar  2017-07-11 12:54:00   \n",
       "2859                                  Kumaraswamy Layout     19-11-2017 15:01   \n",
       "\n",
       "        latitude  longitude lease_type  gym  lift  swimming_pool  ...  \\\n",
       "10720  12.977327  77.501541     ANYONE  0.0   0.0            0.0  ...   \n",
       "10244  12.989211  77.715397     FAMILY  0.0   0.0            0.0  ...   \n",
       "7326   12.959188  77.656335     ANYONE  0.0   0.0            0.0  ...   \n",
       "1436   12.976973  77.670153     ANYONE  0.0   0.0            0.0  ...   \n",
       "2299   12.934838  77.612270     FAMILY  1.0   1.0            0.0  ...   \n",
       "18569  12.934903  77.702967     FAMILY  0.0   1.0            0.0  ...   \n",
       "4541   12.933155  77.636593     ANYONE  0.0   1.0            1.0  ...   \n",
       "18370  12.950288  77.699063     ANYONE  0.0   0.0            0.0  ...   \n",
       "13038  12.900169  77.585651     ANYONE  0.0   0.0            0.0  ...   \n",
       "2859   12.908354  77.561678     ANYONE  0.0   0.0            0.0  ...   \n",
       "\n",
       "       bathroom facing cup_board  floor  total_floor  \\\n",
       "10720       3.0      E       3.0    2.0          3.0   \n",
       "10244       2.0      N       7.0    2.0          4.0   \n",
       "7326        2.0      N       2.0    0.0          1.0   \n",
       "1436        1.0      E       0.0    1.0          1.0   \n",
       "2299        2.0      E       2.0    0.0          7.0   \n",
       "18569       2.0      E       6.0    4.0          5.0   \n",
       "4541        3.0     SW       3.0    1.0          4.0   \n",
       "18370       1.0      E       0.0    3.0          3.0   \n",
       "13038       1.0      N       2.0    3.0          4.0   \n",
       "2859        2.0      N       0.0    2.0          3.0   \n",
       "\n",
       "                                               amenities water_supply  \\\n",
       "10720  {\"LIFT\":false,\"GYM\":false,\"INTERNET\":true,\"AC\"...    CORP_BORE   \n",
       "10244  {\"SC\":true,\"INTERCOM\":true,\"AC\":false,\"PB\":tru...  CORPORATION   \n",
       "7326   {\"LIFT\":false,\"GYM\":false,\"INTERNET\":true,\"AC\"...    CORP_BORE   \n",
       "1436   {\"LIFT\":false,\"GYM\":false,\"INTERNET\":false,\"AC...    CORP_BORE   \n",
       "2299   {\"LIFT\":true,\"GYM\":true,\"INTERNET\":true,\"AC\":t...    CORP_BORE   \n",
       "18569  {\"LIFT\":true,\"GYM\":false,\"INTERNET\":true,\"AC\":...     BOREWELL   \n",
       "4541   {\"LIFT\":true,\"GYM\":false,\"INTERNET\":true,\"AC\":...    CORP_BORE   \n",
       "18370  {\"LIFT\":false,\"GYM\":false,\"INTERNET\":true,\"AC\"...    CORP_BORE   \n",
       "13038  {\"LIFT\":false,\"GYM\":false,\"INTERNET\":true,\"AC\"...    CORP_BORE   \n",
       "2859   {\"LIFT\":false,\"GYM\":false,\"INTERNET\":true,\"AC\"...    CORP_BORE   \n",
       "\n",
       "       building_type  balconies     rent  \n",
       "10720             IF        5.0  17000.0  \n",
       "10244             AP        3.0  23000.0  \n",
       "7326              IF        0.0  24000.0  \n",
       "1436              IF        0.0  13000.0  \n",
       "2299              AP        0.0  35000.0  \n",
       "18569             AP        2.0  25000.0  \n",
       "4541              IF        3.0  38000.0  \n",
       "18370             IF        0.0   8500.0  \n",
       "13038             IF        1.0   9500.0  \n",
       "2859              IF        1.0  14000.0  \n",
       "\n",
       "[10 rows x 25 columns]"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Load the dataset\n",
    "data = pd.read_excel('House_Rent_Train.xlsx')\n",
    "data.sample(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>latitude</th>\n",
       "      <th>longitude</th>\n",
       "      <th>gym</th>\n",
       "      <th>lift</th>\n",
       "      <th>swimming_pool</th>\n",
       "      <th>negotiable</th>\n",
       "      <th>property_size</th>\n",
       "      <th>property_age</th>\n",
       "      <th>bathroom</th>\n",
       "      <th>cup_board</th>\n",
       "      <th>floor</th>\n",
       "      <th>total_floor</th>\n",
       "      <th>balconies</th>\n",
       "      <th>rent</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>12.934471</td>\n",
       "      <td>77.634471</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1250.0</td>\n",
       "      <td>25.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>6.0</td>\n",
       "      <td>12.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>40000.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>12.929557</td>\n",
       "      <td>77.672280</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1400.0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>22000.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>12.982870</td>\n",
       "      <td>80.262012</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1350.0</td>\n",
       "      <td>6.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>5.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>28000.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>12.955991</td>\n",
       "      <td>77.531634</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>600.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>8000.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>12.963903</td>\n",
       "      <td>77.649446</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1500.0</td>\n",
       "      <td>15.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>45000.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    latitude  longitude  gym  lift  swimming_pool  negotiable  property_size  \\\n",
       "0  12.934471  77.634471  1.0   1.0            1.0         0.0         1250.0   \n",
       "1  12.929557  77.672280  0.0   1.0            0.0         1.0         1400.0   \n",
       "2  12.982870  80.262012  0.0   1.0            0.0         0.0         1350.0   \n",
       "3  12.955991  77.531634  0.0   0.0            0.0         1.0          600.0   \n",
       "4  12.963903  77.649446  0.0   0.0            0.0         1.0         1500.0   \n",
       "\n",
       "   property_age  bathroom  cup_board  floor  total_floor  balconies     rent  \n",
       "0          25.0       2.0        2.0    6.0         12.0        2.0  40000.0  \n",
       "1           4.0       2.0        2.0    3.0          4.0        2.0  22000.0  \n",
       "2           6.0       3.0        3.0    1.0          5.0        3.0  28000.0  \n",
       "3           3.0       1.0        1.0    1.0          2.0        0.0   8000.0  \n",
       "4          15.0       3.0        4.0    0.0          0.0        1.0  45000.0  "
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_num = data.select_dtypes(include = ['float64', 'int64'])\n",
    "df_num.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[<AxesSubplot:title={'center':'latitude'}>,\n",
       "        <AxesSubplot:title={'center':'longitude'}>,\n",
       "        <AxesSubplot:title={'center':'gym'}>,\n",
       "        <AxesSubplot:title={'center':'lift'}>],\n",
       "       [<AxesSubplot:title={'center':'swimming_pool'}>,\n",
       "        <AxesSubplot:title={'center':'negotiable'}>,\n",
       "        <AxesSubplot:title={'center':'property_size'}>,\n",
       "        <AxesSubplot:title={'center':'property_age'}>],\n",
       "       [<AxesSubplot:title={'center':'bathroom'}>,\n",
       "        <AxesSubplot:title={'center':'cup_board'}>,\n",
       "        <AxesSubplot:title={'center':'floor'}>,\n",
       "        <AxesSubplot:title={'center':'total_floor'}>],\n",
       "       [<AxesSubplot:title={'center':'balconies'}>,\n",
       "        <AxesSubplot:title={'center':'rent'}>, <AxesSubplot:>,\n",
       "        <AxesSubplot:>]], dtype=object)"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAABRkAAAZACAYAAAD970UkAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/YYfK9AAAACXBIWXMAAA9hAAAPYQGoP6dpAAEAAElEQVR4nOzde3xU1b3///dMEgaIRAjSiJAbJOFiRKSmQuUgqFwar8WAIkZpqJYSsR4UG9pKk8pXQKmn2oYGayUWTmFSi6ZSDAlesFTU4dhqES0Sc5FjUyhqYgmMA7N+f3Cyf0wSYJJJZibJ6/l4+Hhkr7X37PfeYbaTz6y9ts0YYwQAAAAAAAAA7WQPdQAAAAAAAAAAXRtFRgAAAAAAAAABocgIAAAAAAAAICAUGQEAAAAAAAAEhCIjAAAAAAAAgIBQZAQAAAAAAAAQEIqMAAAAAAAAAAJCkREAAAAAAABAQCgyAgAAAAAAAAgIRUZ0muLiYtlsNlVXV7dpu9dff135+fn6/PPPW/RNnjxZkydPtpYbGxuVn5+vV199NaCsp2Oz2ZSfn98prw2g+2vvdbAz5Ofny2az+bStWbNGxcXFnbK/5tdrAAAAhLfmn13nzZunpKQkn3U+/fRT3XLLLfrKV74im82mG2+8UXv37lV+fn5YfOZFaEWGOgDQ3Ouvv66CggLNmzdP/fv39+lbs2aNz3JjY6MKCgokiT9mAeAMvv3tb2vGjBk+bWvWrNF5552nefPmhSYUAAAAwtaDDz6o733vez5tDz30kJ577jk9/fTTGj58uGJjY/Xuu++qoKBAkydPblGURM9CkRFdyujRo0MdAQC6pKFDh2ro0KGhjgEAAIAuYvjw4S3a9uzZo+HDh2vu3LlW27vvvhvMWAhj3C6NoKmoqNANN9ygoUOHqnfv3kpJSdF3vvMd/etf/7LWyc/P15IlSyRJycnJstlsstls1u3Qp95+V11drUGDBkmSCgoKrHWbRuS0NrS7aR/NbxlsaGjQnXfeqYEDB+qcc87RjBkztG/fvlaP48MPP9Stt96qr3zlK3I4HBo1apQKCwsDODMAepKnn35aF198sXr37q3Y2Fh985vf1Pvvv++zzrx583TOOedo//79yszM1DnnnKP4+Hjdd999crvdPuseOHBAWVlZ6tevn/r376+5c+fK5XLJZrP53Ard/NqXlJSk9957Tzt27LCun03XzNPd5v3qq6/6XJMlyRijRx55RImJierdu7fGjRunF198sdVjb2ho0P3336/k5GT16tVLQ4YM0b333qsjR460/UQCwGmUlpZqzJgxcjgcGjZsmB5//HGfa+BVV12lkSNHyhjjs50xRikpKbrmmmsknfysabPZ9Oijj2rVqlVKSkpSnz59NHnyZO3bt08ej0d5eXm64IILdO655+qb3/ymDh48GPTjBYDOcurf1E3XxO3bt+v999+3Pj8WFxdr1qxZkqQpU6b4tKPnYSQjgqayslITJkzQt7/9bZ177rmqrq7WY489pokTJ+pvf/uboqKi9O1vf1uffvqpfv7zn2vz5s0aPHiwpNZHMA4ePFhlZWWaMWOG5s+fr29/+9uSZBUe/WWM0Y033qjXX39dy5YtU0ZGhv785z/rG9/4Rot19+7dq69//etKSEjQT3/6U51//vnatm2b7rnnHv3rX//Sj3/843acGQA9xYoVK/SDH/xAc+bM0YoVK3T48GHl5+drwoQJcrlcSk1Ntdb1eDy6/vrrNX/+fN1333167bXX9NBDD+ncc8/VsmXLJElHjhzRlClT9Omnn2rVqlVKSUlRWVmZbr755rNmee6555SVlaVzzz3XmorC4XC0+ZgKCgpUUFCg+fPnKysrSx9//LHuvPNOnThxQiNGjLDWa2xs1BVXXKEDBw7oBz/4gcaMGaP33ntPy5Yt09/+9jdt3769xRdAANBWZWVlmjlzpiZNmiSn06njx49r9erV+uc//2mt873vfU833HCDXnrpJV199dVW+4svvqjKyko98cQTPq9ZWFioMWPGqLCwUJ9//rnuu+8+XXfddbrssssUFRWlp59+WjU1Nbr//vv17W9/W3/4wx+CdrwAECyDBw/Wrl27tHDhQtXX1+u///u/rfaHH35YP/jBD1RYWKhx48ZJan0UJLo/iowImgULFlg/G2P09a9/XZMnT1ZiYqJefPFFXX/99Ro6dKgSEhIkSZdccskZ53NwOBz66le/KunkbYDjx49vV65t27bplVde0eOPP6577rlHkjR16lT16tVLP/zhD33WXbx4sfr166edO3cqJibGWtftdmvlypW65557NGDAgHblANC9ff7553rooYeUmZmp3/72t1b75MmTlZqaqvz8fOvDmiR9+eWXKigosL4Zvuqqq7R792799re/tYqMzzzzjPbv368XX3zRmm9x2rRpamxs1Nq1a8+Y55JLLlGfPn0UExPT7uvn559/rlWrVumb3/ymnnrqKav9wgsv1OWXX+5TZHziiSf07rvv6s0339Sll15qHdOQIUOUlZWlsrKyVr/cAYC2WLZsmYYMGaJt27apV69ekqQZM2b4fKa89tprNWzYMP3iF7/wKTL+4he/0PDhw1tci/r376/nn39edvvJm8D+9a9/6d5779XIkSNVWlpqrffBBx/oZz/7mRoaGqzPiQDQXTgcDo0fP14xMTH68ssvfT4/Nn1RPnr06HZ/rkT3wO3SCJqDBw9qwYIFio+PV2RkpKKiopSYmChJLW4VDKZXXnlFknzmlJCkW2+91Wf52LFjeumll/TNb35Tffv21fHjx63/MjMzdezYMb3xxhtByw2ga9m1a5eOHj3a4iEr8fHxuvLKK/XSSy/5tNtsNl133XU+bWPGjFFNTY21vGPHDvXr16/FA13mzJnTseFPY9euXTp27FiL6+fXv/516/reZMuWLUpPT9fYsWN9rp/Tp09vcQs2ALTHkSNHtHv3bt14441WgVGSzjnnHJ/rqd1u1913360tW7aotrZW0sk7bsrKyrRw4cIWo6ozMzOtAqMkjRo1SpKs26qbtze9JgAAPQ1FRgSF1+vVtGnTtHnzZj3wwAN66aWX9NZbb1lFuaNHj4Ys2+HDhxUZGamBAwf6tJ9//vkt1jt+/Lh+/vOfKyoqyue/zMxMSfKZXxIATnX48GFJsqaBONUFF1xg9Tfp27evevfu7dPmcDh07Ngxn9eMi4tr8XqttXWGpszNr5ettf3zn//Uu+++2+L62a9fPxljuH4CCNhnn30mY4xf18WcnBz16dNHRUVFkk7eEt2nTx/l5OS02DY2NtZnuamAebr2U6/TAAD0JNwujaDYs2eP3nnnHRUXF+uOO+6w2vfv399p++zdu3eLByRILQuBAwcO1PHjx3X48GGfQmNdXZ3PegMGDFBERISys7OVm5vb6j6Tk5M7IDmA7qjp+vKPf/yjRd8nn3yi8847r12v+dZbb7Vob379aqum4mbza2hr18/T7a+urs7n9sTzzjtPffr00dNPP93qPttz/ABwqgEDBshms/nMv9ik+XXq3HPP1R133KGnnnpK999/v9atW6dbb71V/fv3D1JaAAC6H0YyIiiabjtp/lCB1uYMa1rHn9GNZ1o3KSlJBw8e9Pmg+eWXX2rbtm0+602ZMkWSfOZCk+QzZ5p0clTRlClT9Je//EVjxozRpZde2uK/5qMhAaDJhAkT1KdPH23YsMGn/cCBA3r55Zd11VVXtfk1r7jiCn3xxRctnua8adMmv7Z3OBynvX5K0rvvvuvT3vxhBuPHj1fv3r1bXD9ff/11n9u6pZNzoFVWVmrgwIGtXj/PNAcvAPgjOjpal156qZ5//nl9+eWXVvu///1vbdmypcX6TQ/uy8rK0ueff6677747mHEBoNtoy9/w6N4YyYigGDlypIYPH668vDwZYxQbG6sXXnhBFRUVLda96KKLJEmPP/647rjjDkVFRWnEiBHq169fi3X79eunxMRElZaW6qqrrlJsbKzOO+88JSUl6eabb9ayZct0yy23aMmSJTp27JieeOIJnThxwuc1pk2bpkmTJumBBx7QkSNHdOmll+rPf/6z1q9f32J/jz/+uCZOnKj/+I//0He/+10lJSXpiy++0P79+/XCCy/o5Zdf7qAzBqC76d+/vx588EH94Ac/0O233645c+bo8OHDKigoUO/evdv1dPo77rhD//Vf/6XbbrtNy5cvV0pKil588UXry5RT5xBrzUUXXaRNmzbJ6XRq2LBh6t27ty666CJlZGRoxIgRuv/++3X8+HENGDBAzz33nHbu3Omz/YABA3T//fdr+fLl+va3v61Zs2bp448/Vn5+fovbpe+99179/ve/16RJk/Sf//mfGjNmjLxer2pra1VeXq777rtPl112WZvPAQCc6ic/+YmuueYaTZ8+Xd/73vd04sQJPfroozrnnHP06aef+qyblpamGTNm6MUXX9TEiRN18cUXhyg1AHRt6enpkqQnn3xS/fr1U+/evZWcnMwgnB6IkYwIiqioKL3wwgtKS0vTd77zHc2ZM0cHDx7U9u3bW6w7efJkLV26VC+88IImTpyojIwM/c///M9pX/vXv/61+vbtq+uvv14ZGRnKz8+XdPLW5dLSUn3++efKysrSkiVLNGvWLN1+++0+29vtdv3hD3/Q3Llz9cgjj+jGG2/U66+/rq1bt7bY1+jRo/X2228rPT1dP/rRjzRt2jTNnz9fzz77bLtGIQHoWZYuXaqnnnpK77zzjm688UbdfffduvDCC/X6669bT+Vri+joaL38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dOiQ6dWrlzlx4kSLvkcffdR897vftZZ3795t+vXrZ4w5+UfB6NGjrb6GhgbTu3dv6x9QuOZu7ne/+5256qqrOibw/+ms3P/617/MV7/6VfP55593aJGxM3N/+OGHJiEhodXtOkpn5D506JA555xzzL59+4wxJ4uVl1xySdByv/LKK+a8885rtchYUlJiMjMzreX33nvPJCYmGmOC875E+Bs9erR57rnnjDEni4zPPPOMMcaY2tpaM2TIEPOPf/wjhOm6lqZzeejQIdOnTx+fvvT0dPP73/8+RMnCX1ORcceOHcYYY9555x1zwQUXGLfbbaKjo30+HGdkZFhfjqBr+Oc//2nOPfdcqzjs9XpNXFycqaqq8lnvkUce8fni8Y9//KO54oorgpjUl7+5m8vNzTUPPfRQEBK2ri25X3vtNXPdddeZV155JeR/QPub+1e/+pWZO3duCBK2zt/czz//vLn44otNQ0OD8Xq9ZsmSJeY///M/Q5DY15k+Y4bbe7K74hoZXFwjg4trpP+63e3S/nj88ceVmZkpu73l4V966aWqqKjQP//5TxljtGHDBn3xxRf69NNPVVtbq8TERGvdfv36qV+/fkG7NbO9uU914sQJFRYW6rrrrgtKZimw3Lm5ucrPz9e5554btLxN2pt77969io+P14IFCzRu3DhNmzZNf/nLX8I+93nnnaeioiKNGzdOiYmJysnJUXFxcafnzcvL0/DhwzVz5kz97ne/k81ma7FO8/deUlKS/vd//1derzfk70uE3q5du3T48GFde+21kqR169bpwQcfVEJCgtLS0rRixQqdf/75IU7ZNZx6Ls877zzFxcXp97//vaST0xLs27dP1dXVoQ0Zxmw2m0pKSjRz5kwlJiZq4sSJeuaZZ/TFF1/I6/Vq0KBB1rpJSUmqra0NYVq01ccff6wLLrhAkZGRkk7+vhMSElr8Hlv7f1Yof9f+5j5VXV2dnn32WWVmZgYrZgv+5j5y5Ijuvfde/fKXvwxFzBb8zb1371717t1b1157rcaOHavbb79dhw4dCkVkSf7nvu666zRlyhSdf/75Gjx4sF566SX95Cc/CUVkv4Xbe7K74hoZXFwjg4trpP96XJFxw4YNKikp0dq1a1vtnzx5su677z5dc801mjBhggYPHixJioqKkqQWBRATpHkYAs3dlHXhwoXq37+/Fi1aFPa5f/e736lXr15W4SCYAsnt8Xi0a9cuzZkzR2+//bbuu+8+XXfddUGZaySQ3A0NDVqzZo12796tmpoa/frXv1ZWVlan5165cqUqKytVUlKiJUuW6Msvv2x1vdaKj6frC9b7EuHh6aef1u233279T//RRx/Vo48+qtraWr333nv64Q9/qL///e8hTtk1ND+XpaWleuqppzRu3DitWbNGEydO9Pn/CnwdP35cK1asUGlpqWpqavTSSy/pjjvukMR1qrvw9/d46nrh8Ltuy7+/hoYGXXfddXrggQc0bty4zo52Rv7kXrJkiXJzczVkyJBgxTorf3J7PB5t27ZNa9eu1V/+8hfFx8crNzc3WBFb5U/ut99+Wx988IH+93//V5988omuuuoq3X333cGK2G7h9p7srrhGBhfXyODiGumndo+BDHOtDQfdtGmTSUlJMTU1NX6/zq5du8zQoUONMa3flulwODr9dulAcze5++67zTe+8Q3jdrs7JOupOiP3d7/7XTNkyBCTmJhoEhMTjSSTkJBg3n333bDO7XK5THx8vE//oEGDzjrkvi06I/fvfvc7841vfMOn/7zzzjMfffRR4IH/z5mGaRtjzIgRI8zu3btbtLf1dumOfl8ifP373/82/fr1s+brbO0W36ysLPP000+HIl6X0vxctmbkyJFm+/btQUzVtbhcLjNq1CiftksvvdS8/PLLpm/fvtwu3cX985//NDExMV3yVkB/chtz8v+hEyZMMD/5yU+CnLIlf3NfdNFF1mfFuLg406tXL5/PBcHmb+5HH33UZGdnW8unfrYJBX9z5+bmmlWrVlnLe/bsMQkJCcGM2ipulw49rpHBxTUyuLhG+q/HFBmdTqdJSUkx1dXVZ9226cEXR44cMVOnTjVPPPGEMcaYEydOmGHDhvk8YOLmm28O+9zGGLNo0SIzY8YMc+zYsQ7N26Szcp9KQZiTsSNye71ec+GFF1oT/7tcLjNo0KBOLUZ3RO7/+Z//MXFxceaf//ynMcaY119/3cTGxnZoUfrU3B6Px5r/0Rhj3nzzTTNgwADz6aefttiuoaHBDBo0yOfBL9///veNMcF5XyJ8rVu3zlx++eXW8vHjx82AAQPMq6++aow5WXQcOnSoeeutt0IVsctofi6NMT5zWT755JPmq1/9aqvzpuKkuro6069fP/PBBx8YY07O0Ttg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vt5azxijNWvWaOzYserTp48GDBigrKwsffTRRz6vZ4zRww8/rMTERPXu3VuXXnqpKioqWr2Frra2Vrfddpu+8pWvyOFwaNSoUfrpT38qr9cr6eQ1samIWFBQIJvNJpvNpnnz5klq/XbpiooK3XDDDRo6dKh69+6tlJQUfec73zntbdEff/yxZs6cqZiYGJ177rm67bbbdOjQobOety+//FLLly/XyJEjrf9Xfetb3/JrWwCh03TN+8tf/nLG935SUpKuvfZabd68WZdccol69+5tjares2ePbrjhBg0YMEC9e/fW2LFj9cwzz/js59VXX5XNZtOGDRu0ePFinX/++erTp4+uuOIK/eUvf2mRa/fu3br++usVGxur3r1765JLLlFJSYnPOk3XvPLycuXk5GjQoEHq27evli5dqiVLlkiSkpOTrWvlq6++qvnz5ys2NlaNjY0t9nnllVfqwgsv9PvcffTRR7rlllt0wQUXyOFwKC4uTldddZX++te/Wus0v9bPmzfPytP8v1M/lzc0NOj+++/3+dx477336siRI37nA9AxuE7+/9p6ndy9e7duueUWqzaQlJSkOXPmqKampsW6O3fu1IQJE9S7d2/rb++nnnqq1amAnE6nJkyYoOjoaJ1zzjmaPn16q+cIATDotqZPn24GDRpknnzySfPqq6+a559/3ixbtsxs2rTJfPDBB0aS+e1vf2utP2PGDNOnTx+Tmppqtb355ptGktm6davVJsn8+Mc/tpbXrVtnJJnk5GRz3333mfLycrNq1SoTERFh5syZY8aNG2eWL19uKioqzPe//30jyfz0pz+1tq+qqjKSTGJiornuuuvMli1bzIYNG0xcXJxJS0sz2dnZJicnx7z44oumqKjInHPOOea6667zOdYrrrjCXHHFFS1eMykpycyYMcM8//zz5vnnnzcXXXSRGTBggPn888+tddeuXWskmZtuusls2bLF/Pd//7dJS0sziYmJJjExsU3n/IorrjADBw40F1xwgXniiSfMtm3bzD333GMkmdzcXGu9o0ePmjFjxpjo6GizevVqU15ebh588EETGRlpMjMzrfW8Xq+ZPn26iYyMNA8++KApLy83q1evNtHR0eaSSy4xx44dO+05ABBcP/7xj40kM2LECLNs2TJTUVFhHnvsMeNwOMy3vvUta70777zTREVFmfvuu8+UlZWZ3/72t2bkyJEmLi7O1NXVWestXbrUSDJ33XWXKSsrM7/61a9MQkKCGTx4sM97/eDBg2bIkCFm0KBBpqioyJSVlZm7777bSDLf/e53jTHGHDt2zJSVlRlJZv78+WbXrl1m165dZv/+/caY//86XlVVZb3uL3/5S7NixQrzhz/8wezYscM888wz5uKLLzYjRowwX375ZYvjTkxMNEuWLDHbtm0zjz32mHWdOnXd5tepEydOmBkzZpjo6GhTUFBgKioqzFNPPWWGDBliRo8ebRobGzvq1wOgg/n73k9MTDSDBw82w4YNM08//bR55ZVXzFtvvWU++OAD069fPzN8+HDzm9/8xvzxj380c+bMMZLMqlWrrP288sorRpKJj483N9xwg3nhhRfMhg0bTEpKiomJiTGVlZXWui+//LLp1auX+Y//+A/jdDpNWVmZmTdvnpFk1q1bZ63XdM0bMmSIueuuu8yLL75onn32WVNdXW0WLVpkJJnNmzdb18r6+nrzzjvvGEnmV7/6lc95eO+994wkU1hY6Pe5GzFihElJSTHr1683O3bsML///e/NfffdZ1555RVrnebXy/3791t5mv677bbbjCTjdDqNMcYcOXLEjB071px33nnmscceM9u3bzePP/64Offcc82VV15pvF6v3xkBBI7r5EntuU7+7ne/M8uWLTPPPfec2bFjh9m0aZO54oorzKBBg8yhQ4es9d555x3Tu3dvM2bMGLNp0ybzhz/8wWRmZpqkpKQWn23/3//7f8Zms5mcnByzZcsWs3nzZjNhwgQTHR1t3nvvPb+z4cwoMnZj55xzjrn33ntP2z906FCTk5NjjDHG7Xab6OhoqwhYU1NjjDn5RoyKijL//ve/re1OV2RctGiRz+vfeOONRpJ57LHHfNrHjh1rxo0bZy03FQQvvvhic+LECav9Zz/7mZFkrr/+ep/t7733XiPJ1NfXW22nKzJedNFF5vjx41b7W2+9ZSSZjRs3GmNO/oF7/vnnm8suu8xnHzU1NSYqKqpdRUZJprS01Kf9zjvvNHa73TqvRUVFRpIpKSnxWW/VqlVGkikvLzfGGKso8Mgjj/is53Q6jSTz5JNPnvYcAAiupg+Szd+vCxcuNL179zZer9fs2rWrxRctxhjz8ccfmz59+pgHHnjAGGPMp59+ahwOh7n55pt91mva/tT3el5enpFk3nzzTZ91v/vd7xqbzWb+/ve/G2OMOXToUIvrd5PWioyn8nq9xuP5/9i78/ioyvP//++ZLCNEoiRgQM1mFkAWkRoFpYGALMalNoV8ZAnwAWuRoFZaFKxgolQW6d5gsK2gYGFSpaVFDAkqKK3KUD+INCISs0A1QiMmSGQamPP7g2/OjyEJzDDJZBJez8fDR3Pu+z5nrnuauThz5Zz71BsVFRWNclzDvB9++GG3fV566SVDkrF27Vqz7ew8tW7dOkOS8corr7jt63A4DEnGihUrmowHQNvz9LMfGxtrBAUFmbmowT333GPYbDajsrLSrf22224zOnfubP5BuOHL86BBg9yKZOXl5UZISIhx7733mm29e/c2rr/+eqO+vt7tmHfccYfRs2dP8zyzIedNmTKl0byeeeaZZvPhsGHDjIEDB7q13X///UZ4eLhx7NixJt+ns/3nP/8xJBm//OUvzznufOd1BQUFhsViMR577DGzbfHixYbVajUcDofb2JdffrnRRQMAWh958jRv82RTTp48aXz99ddGWFiY8atf/cpsHz9+vBEWFuZWeDx16pRx7bXXusVYWVlpBAcHN6pZHDt2zOjRo4eRmZl5wbHBHbdLd2A33nijVq9erUWLFundd991u0VZkkaOHKmtW7dKOr14a11dnebMmaNu3bqpuLhYkrR161bzcuLzueOOO9y2+/TpI+n0AwXObm/qMuf09HRZrVa3cc3tL52+PfB8br/9dgUFBZnbAwYMkCTz9T/++GPzdu4zxcTE6JZbbjnv8ZvSpUsX3XXXXW5tEydOlMvl0ltvvSVJeuONNxQWFqZx48a5jWu4dfH11183x53Z3mD8+PEKCwszxwEIHGd//gcMGKATJ07o8OHD2rRpkywWiyZPnqyTJ0+a//Xo0UPXXXed+eTnd999V06ns1FuGjx4cKNlHN544w1de+21uvHGG93ap02bJsMwzDzircOHD2vmzJmKjo5WcHCwQkJCFBsbK0n66KOPGo2fNGmS23ZmZqaCg4P15ptvNvsamzZt0uWXX64777zT7f0YOHCgevTo0eSTsAEEFk8++wMGDFBycrLbuDfeeEMjR45UdHS0W/u0adNUV1end955x6194sSJslgs5nZsbKxuvvlm83UOHDigffv2mfGcmVPS09P1+eef6+OPP3Y75ve+9z2v5vrQQw9p9+7d+vvf/y7p9K3Ja9as0dSpU3XppZd6dIyIiAglJCTomWee0c9//nP93//9n7m0hae2b9+urKwsTZ48WT/96U/N9k2bNqlfv34aOHCg2/zHjBlj3s4IwP/Ik97lSUn6+uuv9eijjyoxMVHBwcEKDg7WpZdequPHj7udh27fvl0jRoxQt27dzDar1droHHrLli06efKkpkyZ4jbvSy65RMOGDSM/tiCKjB2Y3W7X1KlT9fvf/15DhgxRRESEpkyZoqqqKknSrbfeqsrKSn3yySfaunWrrr/+el1xxRUaMWKEtm7dqm+++Ub/+Mc/dOutt3r0ehEREW7boaGhzbafOHHCp/0lNXmMs0VGRrpt22w2SacXrZWk6upqSVJUVFSjfZtq80RT+/Xo0cPt9aqrq9WjRw+3fwQk6YorrlBwcLDbuODg4EYPZLBYLOrRo4c5DkDgOFfe+eKLL2QYhqKiohQSEuL237vvvmuud+hNbqqurm7yqdBXXnml27G84XK5NHr0aG3YsEGPPPKIXn/9de3cudNc07Yhh56pIc81CA4OVmRk5Dlf/4svvtBXX32l0NDQRu9HVVVVs+s/Aggcnnz2m8pR3uaus1+noa1h3BdffCFJ+vGPf9won8yaNUuSGuWUpl7/XL7zne8oLi5OeXl5kk6vWXb8+HG39czPx2Kx6PXXX9eYMWO0bNkyDRo0SN27d9eDDz6oY8eOnXf/f/3rX7r77rv17W9/W3/4wx/c+r744gvt2bOn0fy7dOkiwzDIqUAbIU96lyel0wXT3/72t7r33nu1ZcsW7dy5Uw6HQ927d3c7D62urvbofLlh7ikpKY3mbrfbyY8tiKdLd2DdunXTL3/5S/3yl79UZWWl/vrXv2revHk6fPiwCgsLNXLkSEmnr1YsLi7WqFGjJJ2+wvHxxx/XW2+9JafT6XGRsT1qKAY0JJ0zNRRjvXWuYzW8XmRkpN577z0ZhuFWaDx8+LBOnjxp/iUmMjJSJ0+e1JEjR9wKjYZhqKqqSikpKRcUI4C20a1bN1ksFr399ttm8fFMDW3ny01nXs0YGRmpzz//vNG4zz77zHxNb+3du1cffPCBVq9eralTp5rtBw4caHafqqoqXXXVVeb2yZMnVV1d3ajoeqZu3bopMjJShYWFTfZ36dLF69gB+Jcnn/2z/6gqeZ+7mjovq6qqMl+nYfz8+fOVkZHRZKy9evVy224qrnOxWq3Kzs7WY489pp/97GdasWKFRo4c2ei45xMbG2sWCPfv36+CggLl5OTov//9r/Lz85vd79ChQxo7dqxiYmL0yiuvKCQkxK2/W7du6tSpk55//vkm97+Qfw8A+I486V2erKmp0aZNm/TEE09o3rx5ZrvT6dSXX37pNjYyMtKj7/INc3/55ZfNO3PQOriS8SIRExOj2bNna9SoUXr//fclnf6rxLXXXqtXXnlF//znP80i46hRo3TkyBH9/Oc/V3h4eIcuZPXq1Us9evRo9DStyspK/eMf/7igYx47dkx//etf3dr++Mc/ymq1KjU1VdLpQu7XX3+tv/zlL27jXnzxRbP/zP9du3at27hXXnlFx48fN/sBtA933HGHDMPQv//9b91www2N/uvfv78k6aabbpLNZpPdbnfb/91332203MTIkSNVUlJi5vYGL774oiwWi9LS0iQ1vpL7XBpOKM8uhK5cubLZfV566SW37YKCAp08ebLRk7DPdMcdd6i6ulqnTp1q8v3w9os7AP+7kM++dDp3vfHGG+aX5QYvvviiOnfurMGDB7u1r1u3ToZhmNsVFRX6xz/+Yb5Or169lJSUpA8++KDJfHLDDTd49IeL8+XKe++9V6GhoZo0aZI+/vhjzZ49+7zHPJfk5GQ9/vjj6t+/f6M8fqaamhrddtttslgs2rx5s8LDwxuNueOOO1RaWqrIyMgm53/2chsA/IM86V2etFgsMgyj0Xno73//e506dcqtbdiwYXrjjTfcrkR0uVz605/+5DZuzJgxCg4OVmlpabNzR8vgSsYOqqamRmlpaZo4caJ69+6tLl26yOFwqLCw0O2vFiNHjtRvfvMbderUyVyDMD4+XvHx8SoqKtJdd92l4OCO+2titVqVm5urH/zgBxo3bpymT5+ur776Srm5uerZs6fbGpGeioyM1P3336/KykolJydr8+bN+t3vfqf7779fMTExkqQpU6YoLy9PU6dOVXl5ufr3768dO3bo6aefVnp6unn16KhRozRmzBg9+uijqq2t1S233KI9e/boiSee0PXXX6+srKwWfT8AtK5bbrlF9913n/73f/9Xu3btUmpqqsLCwvT5559rx44d6t+/v+6//35FRERozpw5Wrx4sbp27arvfve7OnToUJO56eGHH9aLL76o22+/XU8++aRiY2P16quvasWKFbr//vvN9X26dOmi2NhYbdy4USNHjlRERIS6devW5JfO3r17KyEhQfPmzZNhGIqIiNDf/vY3c73epmzYsEHBwcEaNWqU/vWvf2nBggW67rrrGq2Jc6Z77rlHL730ktLT0/XQQw/pxhtvVEhIiA4dOqQ333xT3/nOd/Td7373wt9wAK3uQj77kvTEE09o06ZNSktL08KFCxUREaGXXnpJr776qpYtW6bLLrvMbfzhw4f13e9+V9///vdVU1OjJ554Qpdcconmz59vjlm5cqVuu+02jRkzRtOmTdNVV12lL7/8Uh999JHef//9Rl86m9Lwx55f/epXmjp1qkJCQtSrVy/zi/fll1+uKVOm6Nlnn1VsbKzuvPNOr96vPXv2aPbs2Ro/frySkpIUGhqqN954Q3v27HG7YudsEydOVElJiZ577jkdPHhQBw8eNPuuvvpqXX311frhD3+oV155RampqXr44Yc1YMAAuVwuVVZWqqioSD/60Y900003eRUvAN+RJ73Lk+Hh4UpNTdUzzzxjnqtu375df/jDH3T55Ze7jf3JT36iv/3tbxo5cqR+8pOfqFOnTsrPz9fx48clyTxnjouL05NPPqmf/OQn+vTTTzV27Fh17dpVX3zxhXbu3KmwsDDl5uZ6FSea0VZPnEHrOnHihDFz5kxjwIABRnh4uNGpUyejV69exhNPPGEcP37cHLdx40ZDkjFq1Ci3/b///e8bkoxf//rXjY6tZp4uffaT7BqepnXmk54MwzCmTp1qhIWFmdsNT4J+5pln3MY1PCXrT3/6k1t7U6/X3NOlzz5mU/EbhmE899xzRmJiohEaGmokJycbzz//vPGd73zHuP766xvtfy7Dhg0z+vbta2zbts244YYbDJvNZvTs2dN47LHHGj3Bq7q62pg5c6bRs2dPIzg42IiNjTXmz59vnDhxwm3cN998Yzz66KNGbGysERISYvTs2dO4//77jaNHjzZ6bZ4uDbSd5nJeU09ufv75542bbrrJCAsLMzp16mQkJCQYU6ZMMXbt2mWOcblcxqJFi4yrr77aCA0NNQYMGGBs2rTJuO6664zvfve7bq9RUVFhTJw40YiMjDRCQkKMXr16Gc8884z5hMAGW7duNa6//nrDZrMZkoypU6c2G2NJSYkxatQoo0uXLkbXrl2N8ePHG5WVlY1y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aCVeFRlTU1N19dVXN9l333336Re/+EWjtRrsdruys7MlSfHx8UpNTdXGjRvNvpkzZyooKEgRERHKzMzU+vXrzb5p06YpLCxMNptN06dP17p167yeIAD4S3NXe0+fPl29evXSwIEDlZqaqt27d5t9XO0NAAAAAOgIWuTBL88++6z69u2rm266qVFfZWWl25WPcXFxqqysbLZv165dZt+wYcPc+l5++eVmY3A6nXI6neZ2w9Nv6uvrVV9ff945NIyxWY1GbYGsIcb2EOuZiNu/Loa4A2Fu48aN0yOPPKKhQ4e6td9999167rnnFBwcrE2bNikzM1P79++X5H61d1lZmYYMGaK0tDR17drV7WrvmpoaDRo0SCNGjFDv3r3drvYODg7WLbfcoqFDh2rMmI73pD4AAAAAQODzuchYVlam3/3ud/r73//e7BiLxWL+bBhGi/SdbfHixcrNzW3UXlRUpM6dO59z3zM9dYPL/Hnz5s0e79fWiouL2zqEC0Lc/tWR466rq/NDJOeWmpraZPtdd91l/jx48GBVVFTI5XLJarXKbrdr9erVktyv9p42bVqzV3vn5OS4Xe0tybzamyIjAAAAAKAt+FxkfOedd/TZZ5+ZT6qqqqrSjBkztGjRIn3/+99XTEyMysvL1b17d0lSRUWF0tPTJcnsS0lJMftiYmLc+hqc2deU+fPna86cOeZ2bW2toqOjNXr0aIWHh593HvX19SouLtaCXVY5XaeLm3tzAv/LekPco0aNalePVydu/7oY4m64ejnQ/epXv1J6erqs1tOrVbS3q70D4YpRbxC3fxF367IFuf/BteHui/ZytTcAAAA6Np+LjBMnTtTEiRPN7eHDh+vHP/6x7rjjDknS+PHjlZeXp9WrV6usrEzbt29Xfn6+2bdy5UplZGSopqZGdrtdhYWFZt/s2bM1a9YsBQcH6/nnn9eiRYuajcNmszVaD1KSQkJCvCqqOF0WOU9ZzH3bC2/nGSiI2786ctztYV5r165VQUGB3n77bbf29nS1d0e+GjYQEbd/BXrcy25sur29XO0NAACAjs2rImN2drY2btyoqqoq3Xrrrbr00kt14MCBc+4zd+5cTZ8+XYmJibJarcrLy1NERIQkKSsrSw6HQ8nJyebYhisihw8frszMTPXv31+SdM8992js2LFeTxAAAoHdbldubq5ef/11XXHF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MECXXHKJrrnmGv3617++4Ng8OVZlZaUmT56sK664QjabTX369NHPfvYzuVwut3G5ubm66aabFBERofDwcA0aNEh/+MMfZBiG27iGeWzYsEHXX3+9LrnkEvOq9X379mns2LHq3LmzunXrppkzZ+rYsWMXPD8AF69p06Zp6NChkqT/+Z//kcViafYWPU/P9STp+eef13XXXadLLrlEERER+u53v6uPPvqo0Wtfeuml+vDDDzV69Gh16dJFI0eObPE5AujYcnJyNHfuXElSfHy8+Z1427ZtHuWt4cOH69VXX1VFRYXbd+oGnp67eSsuLk6PP/64JCkqKkoWi6XZZdAk6csvv9SsWbN01VVXKTQ0VNdcc41+8pOfyOl0uo3z9Pv7uc414X9cyQifffe731VmZqZmzpypf/3rX1qwYIFKSkr03nvvKSQkRJ988onS09P1wx/+UGFhYdq3b5+WLl2qnTt36o033pAkLViwQMePH9fLL7+sd955xzx2z549zZ9fffVVORwOPfnkk7r00ku1bNkyffe739XHH3+sa665xi2mjIwM3XPPPZo5c6aOHz8uwzB099136/XXX9f8+fP17W9/W3v27NETTzyhd955R++8845sNpsk6f7779dzzz2n2bNn64477lB5ebkWLFigbdu26f3331e3bt3M16mqqtL//u//6pFHHtHVV1+t3/zmN5o+fboOHjyol19+WY899pguu+wyPfnkk7r77rv16aef6sorr2zN/zsAtKEPPvhAQ4cOVbdu3fTkk08qKSlJn3/+uf7617/qv//9r9fH2717t374wx8qJydHPXr00EsvvaSHHnpI//3vf/XjH/+4xY915MgR3Xzzzfrvf/+rp556SnFxcdq0aZN+/OMfq7S0VCtWrDCPV15erh/84AeKiYmRJL377rt64IEH9O9//1sLFy50e+33339fH330kR5//HHFx8crLCxMX3zxhYYNG6aQkBCtWLFCUVFReumll1h/F8AFWbBggW688UZlZ2fr6aefVlpamsLDw1VQUNBorKfneosXL9Zjjz2mCRMmaPHixaqurlZOTo6GDBkih8OhpKQk85j//e9/ddddd+kHP/iB5s2bp5MnT/pt7gA6hnvvvVdffvmlfvOb32jDhg3md+Frr73Wo7y1YsUK3XfffSotLdWf//znRsf35tzNG3/+85+V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+2zAYz/wgQ/o1ltvDdg3nrUQAAAAAEbDG78gJD7wgQ8EbEdERCguLk59fX364x//qI997GO64oortGPHDqWnpysqKsq4j+M777wz5nGH7uv4Xu/y3NfXJ0m65pprRtSuvfZatbS0BOyLiorSFVdcEbDPbrfr3Xfffc85vvnmm/r3f/93RUZGjlofaiYWFxfr3Llz+td//Vd9+tOfls/nU1ZWlnbs2KG8vLz3fA4AmIjh696bb74pv9+v+Pj4UccuWrQoYDsuLm7EGLvd/p5rMgAAAACMhSYjQqK3t1cf/OAHje1z586pr69PcXFx+o//+A+98cYbevbZZ42zFyXp97///SWPu2DBAknS6dOnlZCQMOqYoX8o//a3vx1Re+ONN3T11VdPZCpjuvrqq3XjjTfqq1/96qj1a6+91vj8s5/9rD772c/q7bff1nPPPadHH31Ua9as0YkTJ5SUlBSSPABgsViMz6+++mpZLBb99Kc/ld1uHzF2tH0AAAAAECo0GRES3/nOd3TLLbcY2/X19Tp37pxWrFhh/CP44n/g7t2795LHzc/Pl81m07/8y79o2bJlo45ZtmyZrrzyStXV1WndunXG/tOnT+s//uM/tHbt2suZ0ghr1qzRoUOHlJqaqvnz54/rMdHR0frEJz6h//3f/9Xdd9+tX//61zQZAUyKNWvWaOfOnfrv//5vFRUVheSYQ+s2ZzcCAAAAuBSajAiJhoYGRUREKC8vT7/+9a/1yCOP6KabblJRUZH+8Ic/aP78+dq0aZMeffRRRUZG6jvf+Y5++ctfXvK4ycnJ+pu/+Rs99thjeuedd7R+/XpdddVVam9v1//8z/+osrJS8+bN0yOPPKK/+Zu/0X333af169err69PlZWVuuKKK/Too4+GZI5/+7d/q5aWFn30ox/Vww8/rOuuu07vvvuuurq6dOjQIdXU1GjhwoX6y7/8S1155ZW67bbbdM0116i3t1dVVVW66qqrlJWVFZIsAHCx2267TQ8++KA++9nPqq2tTTk5OYqOjtZvf/tbHTt2TDfccIP+z//5PxM6Zmpqqq688kp95zvf0ZIlSzR37lxde+21AWduAwAAAIAk8cYvCImGhga98sorKiws1Pbt23XXXXepublZc+bMUVxcnH70ox8pKipK9957r0pKSjR37ly5XK5xHftv//Zv9e1vf1vd3d3a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dtx0zjUb5vmbGM4FXM+7776rj3/84/EOY8bE8z3yRsb/vM8lczW36cprpt/r5/p64032+5Zs75EAAACYORZjFv+T9uDgoJxOp4aGhpSamirDMLR48WL97Gc/m3CXTiAQ0Ntvv62FCxeG/CU8nJGREeXk5OjChQvKzMyMdSoxR7zTL9FiTvZ4DcPQu+++q5tvvllWqzUGEc5+M/keORmJ9lqcjLma21zNSyK3Mcn4HgkAAICZNat3Mt5000268847deTIEW3btk0//OEPlZeXF/azxmw2m2w2W9C5+fPnT3rNzMzMhPpLCPFOv0SLOZnjTbbdOfF4j5yMRHstTsZczW2u5iWRm5R875EAAACYWbO6yChJBw8e1LZt2/TMM88oMzNTL7zwQrxDAoBZg/dIAAAAAMBsMOuLjEuXLtVrr70W7zAAYFbiPRIAAAAAMBvwoTz/n81m05NPPhlyO+FsRbzTL9FiJl7MFnP5eztXc5ureUnkBgAAAMyUWf3gFwAAAAAAAACzHzsZAQAAAAAAAESFIiMAAAAAAACAqFBkBAAAAAAAABCVpCsynjt3Tp/+9KdVWFiou+++W2fOnAnb7zvf+Y6cTqcKCgr02GOP6cMPP5zhSKUPPvhADzzwgAoLC1VcXKzy8nL19vaG9Hv11VeVnp6u4uJi87/Lly/PeLySlJeXp2XLlplxuN3usP1mw/WVpD//+c9B162wsFCpqal6++23g/rF8xp/8YtfVF5eniwWi06fPm2eHxwcVHl5uZxOp4qKitTd3X3dOV566SUtW7ZMDodDDz74oN57770Zj7empkZLly5VcXGxysrK9MYbb4Qd39vbq9TU1KBr3dPTM23xItRUXnOjo6OqqqqSw+FQYWGhWltbzbZAIKCdO3eqoKBADodDBw4cCFrv6aefVkFBgQoKCvTEE09Ma243el9N9Pw2bNig22+/XcXFxfrsZz9r/owlel7XamxsDHpdzoXcrvd7cy7kBgAAgCRjJJm1a9cahw4dMgzDML7//e8bpaWlIX3eeustY/HixcbAwIARCASM+++/32hqaprhSA3j8uXLxssvv2wEAgHDMAzjm9/8prF+/fqQfq+88opx1113zXR4YeXm5hq//vWvb9hntlzfcP75n//Z+PznPx9yPp7XuKury7hw4ULItf3bv/1b48knnzQMwzBef/11w263G36/P2T8u+++a9x0003Gb37zG8MwDKO2ttaor6+f8Xjb2trM+P7zP//TcDqdYcd7vV5j4cKF0xYfJjaV11xjY6OxdetWwzCu/oxnZ2cbb7/9tmEYhvHCCy8Y69atMz788ENjaGjIyM3NNV+PXV1dxooVK4z33nvP+OCDD4y77rrLaG9vn7bcbvS+muj5vfPOO+aff/SjHxl33nnnnMhrzH//938b5eXlht1uN1+XcyG36/3enAu5AQAAILkk1U7GwcFBnTp1Sg8//LAk6cEHH5TX6w3ZHfiDH/xAf/VXf6Xs7GxZLBZt375dL7744ozH+5GPfEQVFRWyWCySpNLSUr311lszHkeszZbrG86hQ4f06KOPxjuMIGVlZbr11ltDzre0tKi2tlaSVFJSouzs7LC7GX/84x9r1apVWrZsmSRpx44d03q9rxfvF77wBaWmpkq6+lru6+tTIBCYtjgwdVN5zbndbrMtPz9fZWVlamtrM9u2b9+ulJQUZWVlacuWLTp69KjZtm3bNmVkZMhms6mmpmZaX583el9N9Pzmz59v/nl4eFhWq3VO5CVJPp9PtbW1OnDggPm9myu5Xc9czg0AAABzU1IVGS9cuKCbb77ZLHRYLBbZ7Xb19/cH9evv71dubq55nJeXF9InHp5//nndf//9Ydt++9vfauXKlSopKQm5NWqmPfTQQ/rkJz+pv/u7v9OlS5dC2mfr9X3ttdc0NDSkz3/+82HbZ9M1HhoaUiAQ0KJFi8xz17uO4a737373u7gW+P7lX/5FFRUVZhFkvJGREZWUlGjlypX6+te/ritXrsxwhBhvotfcjX6up9o2E8beV+dKfo888ohycnL01a9+VS+88MKcyetrX/uaHn74YeXn55vn5kpuUujvzbmUGwAAAJJHUhUZJQXtgJAkwzAm7He9PjPpmWee0blz5/RP//RPIW0rV67UxYsXderUKf3oRz9SU1OTWlpa4hCl9JOf/ES//OUvderUKS1cuFBbt24N22+2XV9J+u53v6tHHnnELEJfazZd4zGRvpbD9Y2nI0eOqKWlRQcPHgzbvnjxYl28eFEej0cnTpzQT3/6Uz333HMzHCXCmeg1d6Of66m2Tafx76tzIb/vfe97unDhgp5++mnV1dWFrD/Z+GZDXq+99po8Ho927NgR0pbouUnX/705F3IDAABAckmqImNOTo4uXrxoPmTEMAxduHBBdrs9qJ/dbg+6hbqvry+kz0zav3+/Wltb9eMf/1jp6ekh7ZmZmfr4xz8uSbr11ltVVVWln/70pzMdpiSZ1yktLU1f+tKXwsYx266vJL3//vtyu92qqakJ2z6brrEkLVy4UJKCdope7zqOv969vb265ZZbrruLcDq53W41Njaqs7NTN910U9g+NpvNbMvKylJNTU1crzWumug1d6Of66m2Tafx76tzLb+tW7fqlVdeMY8TOa+uri69+eabys/PV15eni5evKiNGzfq9ddfT/jcxtaTgn9vzrXXIwAAAJLEjH364yzxF3/xF0EPfvnUpz4V0qenpyfkwST/9m//NsORXvXcc88ZK1euND/QPZzf//73xpUrVwzDMIyRkRHj05/+tPGd73xnpkI0vffee0EPHnjuueeMz372syH9ZtP1HXPo0CHjM5/5zHXbZ8M1Hv9wgK1btwY9FCAnJyfsg19GRkaMRYsWBT345Stf+cqMx+t2uw2Hw2H09vbecNwf//hH43/+538MwzCMDz74wKisrDSeeOKJaY0V4U3mNffkk08GPYjipptuMoaGhgzDuPrzde+995oPorDb7caZM2cMw7j6UKXbbrst6EEUP/7xj6c1r+u9ryZyfsPDw8bvfvc787i1tdW45ZZbjEAgkNB5hXPt6zLRc7vR781Ezw0AAADJJ+mKjG+++aZRWlpqOJ1O46677jJOnz5tGIZhPProo0ZbW5vZ71vf+pZRUFBg5OfnG48++qhZ9JhJFy5cMCQZS5YsMe644w7jjjvuMO6+++6QeL/5zW8aK1asMG6//XZjxYoVxpNPPmk+OXUm9fT0GMXFxcYnP/lJo6ioyPjCF75geL3ekHgNY3Zc32utWbPG+O53vxt0brZc4x07dhi33HKLkZKSYmRnZxsFBQWGYRjGwMCAsX79esPhcBgrVqwwXn31VXPME088EVS4bWtrM5YuXWoUFBQYDzzwgDE8PDzj8aamphq33nqr+Vq+4447jD/96U8h8f7whz80brvtNvNaP/7448YHH3wwbfEi1FRec++9956xZcsWo6CgwHA6ncb3v/99s+3DDz80duzYYSxZssRYsmSJ8c1vfjNovcbGRiM/P9/Iz883du/ePa253eh9NZHz6+/vN0pKSoyioiLj9ttvN+69917jF7/4RcLnFc61RcZEz+1GvzcTPTcAAAAkH4th8IE8AAAAAAAAAKYuqT6TEQAAAAAAAEDsUWQEAAAAAAAAEBWKjAAAAAAAAACiQpERAAAAAAAAQFQoMgIAAAAAAACICkVGAAAAAAAAAFGhyAgAAAAAAAAgKhQZAQAAAAAAAESFIiMAAAAAAACAqFBkBAAAAAAAABAViowAAAAAAAAAovL/AKCTKFQEvUzCAAAAAElFTkSuQmCC",
      "text/plain": [
       "<Figure size 1600x2000 with 16 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "df_num.hist(figsize=(16, 20), bins=50, xlabelsize=8, ylabelsize=8)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 20555 entries, 0 to 20554\n",
      "Data columns (total 25 columns):\n",
      " #   Column           Non-Null Count  Dtype  \n",
      "---  ------           --------------  -----  \n",
      " 0   id               20555 non-null  object \n",
      " 1   type             20528 non-null  object \n",
      " 2   locality         20395 non-null  object \n",
      " 3   activation_date  20532 non-null  object \n",
      " 4   latitude         20532 non-null  float64\n",
      " 5   longitude        20532 non-null  float64\n",
      " 6   lease_type       20532 non-null  object \n",
      " 7   gym              20555 non-null  float64\n",
      " 8   lift             20555 non-null  float64\n",
      " 9   swimming_pool    20555 non-null  float64\n",
      " 10  negotiable       20555 non-null  float64\n",
      " 11  furnishing       20555 non-null  object \n",
      " 12  parking          20555 non-null  object \n",
      " 13  property_size    20555 non-null  float64\n",
      " 14  property_age     20532 non-null  float64\n",
      " 15  bathroom         20532 non-null  float64\n",
      " 16  facing           20532 non-null  object \n",
      " 17  cup_board        20532 non-null  float64\n",
      " 18  floor            20532 non-null  float64\n",
      " 19  total_floor      20532 non-null  float64\n",
      " 20  amenities        20532 non-null  object \n",
      " 21  water_supply     20532 non-null  object \n",
      " 22  building_type    20532 non-null  object \n",
      " 23  balconies        20532 non-null  float64\n",
      " 24  rent             20532 non-null  float64\n",
      "dtypes: float64(14), object(11)\n",
      "memory usage: 3.9+ MB\n"
     ]
    }
   ],
   "source": [
    "data.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "id                   0\n",
      "type                27\n",
      "locality           160\n",
      "activation_date     23\n",
      "latitude            23\n",
      "longitude           23\n",
      "lease_type          23\n",
      "gym                  0\n",
      "lift                 0\n",
      "swimming_pool        0\n",
      "negotiable           0\n",
      "furnishing           0\n",
      "parking              0\n",
      "property_size        0\n",
      "property_age        23\n",
      "bathroom            23\n",
      "facing              23\n",
      "cup_board           23\n",
      "floor               23\n",
      "total_floor         23\n",
      "amenities           23\n",
      "water_supply        23\n",
      "building_type       23\n",
      "balconies           23\n",
      "rent                23\n",
      "dtype: int64\n"
     ]
    }
   ],
   "source": [
    "#chaking NA values \n",
    "data['activation_date'] = pd.to_datetime(data['activation_date'])\n",
    "nan_counts_per_column = data.isna().sum()\n",
    "print(nan_counts_per_column)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "id                 0.000000\n",
      "type               0.131355\n",
      "locality           0.778399\n",
      "activation_date    0.111895\n",
      "latitude           0.111895\n",
      "longitude          0.111895\n",
      "lease_type         0.111895\n",
      "gym                0.000000\n",
      "lift               0.000000\n",
      "swimming_pool      0.000000\n",
      "negotiable         0.000000\n",
      "furnishing         0.000000\n",
      "parking            0.000000\n",
      "property_size      0.000000\n",
      "property_age       0.111895\n",
      "bathroom           0.111895\n",
      "facing             0.111895\n",
      "cup_board          0.111895\n",
      "floor              0.111895\n",
      "total_floor        0.111895\n",
      "amenities          0.111895\n",
      "water_supply       0.111895\n",
      "building_type      0.111895\n",
      "balconies          0.111895\n",
      "rent               0.111895\n",
      "dtype: float64\n"
     ]
    }
   ],
   "source": [
    "# NA values %\n",
    "nan_percentage_per_column = (data.isna().sum() / len(data)) * 100\n",
    "print(nan_percentage_per_column)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Fill Na Values with mode and median\n",
    "columns_cata = ['type', 'locality', 'activation_date', 'lease_type', 'furnishing', 'facing', 'amenities', 'water_supply', 'building_type','parking']\n",
    "\n",
    "for col in columns_cata:\n",
    "    mode_value = data[col].mode()[0]\n",
    "    data[col].fillna(mode_value, inplace=True)\n",
    "columns_int=set(data.columns) - set(columns_cata) - set(['id'])\n",
    "for col in columns_int:\n",
    "    median_value = data[col].median()\n",
    "    data[col].fillna(median_value, inplace=True)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "id                 0.0\n",
      "type               0.0\n",
      "locality           0.0\n",
      "activation_date    0.0\n",
      "latitude           0.0\n",
      "longitude          0.0\n",
      "lease_type         0.0\n",
      "gym                0.0\n",
      "lift               0.0\n",
      "swimming_pool      0.0\n",
      "negotiable         0.0\n",
      "furnishing         0.0\n",
      "parking            0.0\n",
      "property_size      0.0\n",
      "property_age       0.0\n",
      "bathroom           0.0\n",
      "facing             0.0\n",
      "cup_board          0.0\n",
      "floor              0.0\n",
      "total_floor        0.0\n",
      "amenities          0.0\n",
      "water_supply       0.0\n",
      "building_type      0.0\n",
      "balconies          0.0\n",
      "rent               0.0\n",
      "dtype: float64\n"
     ]
    }
   ],
   "source": [
    "# NA values %\n",
    "nan_percentage_per_column = (data.isna().sum() / len(data)) * 100\n",
    "print(nan_percentage_per_column)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "#categorical variable\n",
    "#Extract the amenities column and convert it from a JSON-like string to a dictionary\n",
    "data['amenities'] = data['amenities'].apply(json.loads)\n",
    "#Extract amenities and create new columns\n",
    "amenities_list = ['LIFT', 'GYM', 'INTERNET', 'AC', 'CLUB', 'INTERCOM', 'POOL', 'CPA', 'FS', 'SERVANT', 'SECURITY', 'SC', 'GP', 'PARK', 'RWH', 'STP', 'HK', 'PB', 'VP']\n",
    "for amenity in amenities_list:\n",
    "    data[amenity] = data['amenities'].apply(lambda x: 1 if amenity in x and x[amenity] else 0)\n",
    "#Drop the original 'amenities' column if no longer needed\n",
    "data.drop('amenities', axis=1, inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAA/EAAAOfCAYAAACAP0O/AAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/YYfK9AAAACXBIWXMAAA9hAAAPYQGoP6dpAAEAAElEQVR4nOzdeXhN1+L/8c/JdDInYkpoCEIEVXMbaYmiSlt0MFRbUqpVRY0lbRFDq+apNXQgbrm3k3LVVbeqojUTtFqhqjR6G6VFzBnP74/+nK/TJKZYSU68X8+zn8fZe+3PXns757DOWntti81mswkAAAAAABR7LkVdAQAAAAAAcG1oxAMAAAAA4CRoxAMAAAAA4CRoxAMAAAAA4CRoxAMAAAAA4CRoxAMAAAAA4CRoxAMAAAAA4CRoxAMAAAAA4CRoxAMAAAAA4CRoxAMACt13332np59+WlWqVJGnp6d8fX3VoEEDTZo0SSdOnCjq6jlITEyUxWJRYmLide+7d+9excfH6/Dhw7m2xcbGKiwsrMD1uxEWi0X9+vXLc9snn3xyw+d7rc6fP6/4+HijxwAAoKSiEQ8AKFTvvPOOGjZsqO3bt2vYsGFavXq1li1bpk6dOmnevHnq1atXUVfxptm7d6/GjBmTZyN+5MiRWrZsWeFXqhg4f/68xowZQyMeAIAb4FbUFQAA3Do2b96s559/Xq1bt9by5ctltVrt21q3bq0hQ4Zo9erVN+VY58+fl7e3d6712dnZysrKcjh2UahWrVqRHh8AADgneuIBAIXm9ddfl8Vi0dtvv51nI9rDw0Pt27e3v87JydGkSZNUs2ZNWa1WlStXTt27d9evv/7qsF9MTIzq1Kmjr7/+Wk2bNpW3t7d69uypw4cPy2KxaNKkSRo/fryqVKkiq9WqdevWSZJ27Nih9u3bKygoSJ6enqpfv74++uijq57Hjh071LVrV4WFhcnLy0thYWF6/PHH9csvv9jLJCQkqFOnTpKkFi1ayGKxyGKxKCEhQVLew+kvXryouLg4ValSRR4eHqpYsaJeeOEFnTp1yqFcWFiYHnzwQa1evVoNGjSQl5eXatasqQULFly17jfqWq7V8ePH1bdvX9WqVUu+vr4qV66c7r33Xn3zzTf2MocPH1bZsmUlSWPGjLFfl9jYWElSfHy8LBaLvvvuO3Xq1EkBAQEKCgrS4MGDlZWVpf379+v++++Xn5+fwsLCNGnSJIc6XLx4UUOGDFG9evXs+0ZFRenf//53rnO6dFvB/PnzVaNGDVmtVtWqVUsffPDBTb56AADcPPTEAwAKRXZ2tr766is1bNhQoaGh17TP888/r7ffflv9+vXTgw8+qMOHD2vkyJFKTEzUzp07VaZMGXvZ1NRUPfnkk3rppZf0+uuvy8Xl/36nnjVrlmrUqKEpU6bI399f1atX17p163T//ffrzjvv1Lx58xQQEKAPPvhAXbp00fnz5+2NyrwcPnxYERER6tq1q4KCgpSamqq5c+eqcePG2rt3r8qUKaMHHnhAr7/+ul5++WW99dZbatCggaT8e+BtNps6duyotWvXKi4uTvfcc4++++47jR49Wps3b9bmzZsdfvj49ttvNWTIEI0YMULly5fXu+++q169eik8PFzNmjW76rW12WzKysrKtT4nJyfXumu9VpfmMxg9erSCg4N19uxZLVu2TDExMVq7dq1iYmIUEhKi1atX6/7771evXr30zDPPSJK9YX9J586d9eSTT+q5557TmjVrNGnSJGVmZurLL79U3759NXToUP3zn//U8OHDFR4erkceeUSSlJ6erhMnTmjo0KGqWLGiMjIy9OWXX+qRRx7RwoUL1b17d4fjrFixQuvWrdPYsWPl4+OjOXPm6PHHH5ebm5see+yxq15HAAAKnQ0AgEJw9OhRmyRb165dr6l8cnKyTZKtb9++Duu3bt1qk2R7+eWX7euaN29uk2Rbu3atQ9lDhw7ZJNmqVatmy8jIcNhWs2ZNW/369W2ZmZkO6x988EFbSEiILTs722az2Wzr1q2zSbKtW7cu37pmZWXZzp49a/Px8bHNnDnTvv7jjz/Od98ePXrYKleubH+9evVqmyTbpEmTHMp9+OGHNkm2t99+276ucuXKNk9PT9svv/xiX3fhwgVbUFCQ7bnnnsu3npdIuupyeZ2v9VrldV0yMzNtLVu2tD388MP29cePH7dJso0ePTrXPqNHj7ZJsk2dOtVhfb169WySbJ9++ql9XWZmpq1s2bK2Rx55JN9zvVSHXr162erXr5/rOnh5edmOHj3qUL5mzZq28PDwfDMBAChKDKcHABRLl4a8/71HvEmTJoqMjNTatWsd1pcqVUr33ntvnlnt27eXu7u7/fVPP/2kffv26YknnpAkZWVl2Zd27dopNTVV+/fvz7duZ8+etfcAu7m5yc3NTb6+vjp37pySk5Nv5HT11VdfScp9vp06dZKPj0+u861Xr54qVapkf+3p6akaNWo4DOm/ks6dO2v79u25lokTJzqUu95rNW/ePDVo0ECenp5yc3OTu7u71q5de93X5cEHH3R4HRkZKYvForZt29rXubm5KTw8PNc5f/zxx4qOjpavr6+9Du+9916edWjZsqXKly9vf+3q6qouXbrop59+ynXbBgAAxQHD6QEAhaJMmTLy9vbWoUOHrqn8n3/+KUkKCQnJta1ChQq5Gm55lctv2++//y5JGjp0qIYOHZrnPn/88Ue+ed26ddPatWs1cuRINW7cWP7+/rJYLGrXrp0uXLiQ735X8ueff8rNzS3XsHKLxaLg4GD79bikdOnSuTKsVus1H79s2bJq1KhRrvV/n0n/eq7VtGnTNGTIEPXp00fjxo1TmTJl5OrqqpEjR153Iz4oKMjhtYeHh7y9veXp6Zlr/enTp+2vP/30U3Xu3FmdOnXSsGHDFBwcLDc3N82dOzfPOQOCg4PzXffnn3/qtttuu656AwBgGo14AEChcHV1VcuWLfX555/r119/vWrj6FIjNTU1NVfZ3377zeF+eOmvxm5+/r7t0r5xcXH2e6n/LiIiIs/1aWlpWrlypUaPHq0RI0bY11+6F/tGlS5dWllZWTp+/LhDQ95ms+no0aNq3LjxDWcXxPVcq8WLFysmJkZz58512H7mzBmzlbzM4sWLVaVKFX344YcOf+/p6el5lj969Gi+6/L6oQQAgKLGcHoAQKGJi4uTzWZT7969lZGRkWt7ZmamPvvsM0myD41fvHixQ5nt27crOTlZLVu2vOF6REREqHr16vr222/VqFGjPBc/P78897VYLLLZbLlm13/33XeVnZ3tsO5SmWvpHb90Pn8/36VLl+rcuXMFOt+CuJ5rZbFYcl2X7777Tps3b3ZYdz3X5XpZLBZ5eHg4NOCPHj2a5+z0krR27Vr7aAPprwkYP/zwQ1WrVo1eeABAsURPPACg0ERFRWnu3Lnq27evGjZsqOeff161a9dWZmamdu3apbffflt16tTRQw89pIiICD377LOaPXu2XFxc1LZtW/vs9KGhoRo0aFCB6jJ//ny1bdtWbdq0UWxsrCpWrKgTJ04oOTlZO3fu1Mcff5znfv7+/mrWrJkmT56sMmXKKCwsTOvXr9d7772nwMBAh7J16tSRJL399tvy8/OTp6enqlSpkmcPb+vWrdWmTRsNHz5cp0+fVnR0tH12+vr16+upp54q0PkWxLVeqwcffFDjxo3T6NGj1bx5c+3fv19jx45VlSpVHGbC9/PzU+XKlfXvf/9bLVu2VFBQkP1aFtSDDz6oTz/9VH379tVjjz2mI0eOaNy4cQoJCdGBAwdylS9TpozuvfdejRw50j47/b59+3jMHACg2KIRDwAoVL1791aTJk00ffp0TZw4UUePHpW7u7tq1Kihbt26qV+/fvayc+fOVbVq1fTee+/prbfeUkBAgO6//35NmDChwEOdW7RooW3btum1117TwIEDdfLkSZUuXVq1atVS586dr7jvP//5T7344ot66aWXlJWVpejoaK1Zs0YPPPCAQ7kqVapoxowZmjlzpmJiYpSdna2FCxfm+fg6i8Wi5cuXKz4+XgsXLtRrr72mMmXK6KmnntLrr7+eq4e7MF3rtXrllVd0/vx5vffee5o0aZJq1aqlefPmadmyZUpMTHTIfO+99zRs2DC1b99e6enp6tGjhxISEgpc16efflrHjh3TvHnztGDBAlWtWlUjRozQr7/+qjFjxuQq3759e9WuXVuvvvqqUlJSVK1aNS1ZskRdunQpcF0AADDBYrPZbEVdCQAAgMJmsVj0wgsv6M033yzqqgAAcM24Jx4AAAAAACdBIx4AAAAAACfBPfEAAOCWxB2FAABnRE88AAAAAACSvv76az300EOqUKGCfdLZq1m/fr0aNmwoT09PVa1aVfPmzTNaRxrxAAAAAABIOnfunO64445rnvT00KFDateune655x7t2rVLL7/8sgYMGKClS5caqyOz0wMAAAAA8DcWi0XLli1Tx44d8y0zfPhwrVixQsnJyfZ1ffr00bfffqvNmzcbqRc98QAAAACAEik9PV2nT592WNLT029a/ubNm3Xfffc5rGvTpo127NihzMzMm3acyzGx3S3sP+4RxrIzNu41krvngLmBI1lZOcay3dzM/F529oyZLwZJcnM3U2er1dxvh+fOZhnJtRj8udNisRjJNTnIKiDAw0huZqa5z2COuWi5uZv5O0w7lWEkVzL3neTl5WokV5I8PMzUOSvb3Gclx1B2tsE6m8o29Z6TpAvnzXz3S1JGZraRXFdXM98bkuTj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l81my/fYBw8e1PLly7Vy5UqtXLlS69ev1xtvvGHfPnjwYG3cuFErVqzQmjVr9M0332jnzp3Xc+k0efJk1a1bVzt37lRcXJwGDRqkNWvWSJJsNps6duyoEydOaP369VqzZo0OHjyoLl262PdftmyZXnzxRQ0ZMkTff/+9nnvuOT399NNat27dddUDAAAAAG42i4ulWC4l0XUNp09NTVVWVpYeeeQRVa5cWZJ0++23S5KaNWumxMREPfroo0pMTFSPHj20aNEi7d27VzVq1NCmTZs0aNCgfLMzMzPtPc2S9Nhjj+n999/X77//Ll9fX9WqVUstWrTQunXrHBq37dq103PPPSdJGjVqlObOnavGjRvbRwEMHz5cUVFR+v333/Mdwp+Tk6OEhAT5+flJkp566imtXbtWr732ms6cOaNFixbpn//8p1q2bClJWrhwoSpUqHA9l07R0dEaMWKEJKlGjRrauHGjpk+frtatW+vLL7/Ud999p0OHDik0NFSS9P7776t27dravn27GjdurClTpig2NlZ9+/aV9NcPC1u2bNGUKVPUokWL66oLAAAAAMA5XVdP/B133KGWLVvq9ttvV6dOnfTOO+/o5MmTkqSYmBglJiZKktavX68WLVqoWbNmWr9+vbZv364LFy4oOjo632xvb297A16Sypcvr7CwMPn6+jqsO3bsmMN+devWddgu/d8PC5ev+/t+lwsLC7M34CUpJCTEXv7nn39WZmammjRpYt8eEBCgiIiIfPPyculWgstfJycnS5KSk5MVGhpqb8BLUq1atRQYGOhQ5u/XLzo62r79atLT03X69GmHJSsz/brOAQAAAABQtK6rEe/q6qo1a9bo888/V61atTR79mxFRETo0KFDiomJ0Q8//KCffvpJ33//ve655x41b95c69evV2Jioho2bOjQUP47d3d3h9cWiyXPdTk5OfnuZ7FY8l339/2uduxL5S8Nw7+Uc8mVhudfq0uZNpstV35e6/OqQ1775WXChAkKCAhwWL5ZMbEAtQcAAACAv1hcXIrlUhJd91lZLBZFR0drzJgx2rVrlzw8PLRs2TLVqVNHpUuX1vjx43XHHXfI39/foRF/pfvhi7Nq1arJ3d1d27Zts687ffq0Dhw4cF05W7ZsyfW6Zs2akv7qdU9JSdGRI0fs2/fu3au0tDRFRkZKkiIjI7VhwwaHjE2bNtm3X01cXJzS0tIclnvaD7+ucwAAAAAAFK3ruid+69atWrt2re677z6VK1dOW7du1fHjxxUZGSmLxaJmzZpp8eLF9nvf69atq4yMDK1du1YvvviikRMwzc/PTz169NCwYcMUFBSkcuXKafTo0XJxcbnmXnBJ2rhxoyZNmqSOHTtqzZo1+vjjj/Wf//xHktSqVSvVrVtXTzzxhGbMmKGsrCz17dtXzZs3V6NGjSRJw4YNU+fOndWgQQO1bNlSn332mT799FN9+eWX13R8q9Uqq9XqsM7NPeua6w8AAAAAKHrX1RPv7++vr7/+Wu3atVONGjX06quvaurUqWrbtq0kqUWLFsrOzlZMTIykv3rt77nnHknS3XfffXNrXoimTZumqKgoPfjgg2rVqpWio6MVGRkpT0/Pa84YMmSIkpKSVL9+fY0bN05Tp05VmzZtJP11nZYvX65SpUqpWbNmatWqlapWraoPP/zQvn/Hjh01c+ZMTZ48WbVr19b8+fO1cOFC+7UGAAAAgKJS1LPQ30qz01tsN+Pm7lvMuXPnVLFiRU2dOlW9evW6avmwsDANHDjwmp8rX1jGLjHXE9+kdv5zEBRE4+V9jeRKkndzc7P8f3XfWCO5m+Z/ZyRXkh6MMjPx4fipKUZyJWn88LyfQFFQH6zzMZIrSYOa7TOSG/i/PUZyJel/Vcz8KOuTkWYkV5J8Tx25eqEblLPpKyO5k4ImGcmVpLoR1zUQ75q1TuxnJFeSrNExRnJ39n/j6oVuUIPZI4zkumReNJIrSeuCHjeS28R9u5FcSZq+o5Gx7PubZBrJzbaZa1iEeP5hJLfUxVQjuZJ00SP/ebMKotSfPxnJlaSLvmWN5JapE3X1QsXUkb6PFnUV8hQ6Z2lRV+GmM/OveAmza9cu7du3T02aNFFaWprGjv2rQdahQ4cirhkAAAAA4FZCI/4aTZkyRfv375eHh4caNmyob775RmXKlNE333xjv50gL2fPni3EWgIAAABA4SupM8EXRzTir0H9+vWVlJSU57ZGjRpp9+7dV9z/8OHDN79SAAAAAIBbDo34AvLy8lJ4eHhRVwMAAAAAcAugEQ8AAAAAKJjrePw2CoYbFwAAAAAAcBI8Yu4W9tK8C8ayMzKzjeR6e7sbyZWc88fDps/VNZb93ZK9RnKzss195Xi4m/ldMi3NzCOGJCkjw8xnxdXV3Bva09PMIC4fH1cjuZJ06pS5v0NTzpwx85hHSfLzsxrLNsXF0HvalmPuO8nHx8xnJTPTzGNcJen8eTOPn3V1Nddv5OVt7rsjx9C/WabezyZlZph735liMfifO1P/zo56wnkHSv/av3NRVyFPt83+qKircNM577sEAAAAAFAsWFyc78cpZ8VwegAAAAAAnASNeAAAAAAAnATD6QEAAAAABWJxoX+4sHClAQAAAAD4/+bMmaMqVarI09NTDRs21DfffHPF8kuWLNEdd9whb29vhYSE6Omnn9aff/5prH404m+y2NhYdezY8ZrLHz58WBaLRbt37863TGJioiwWi06dOlXg+gEAAAAA8vbhhx9q4MCBeuWVV7Rr1y7dc889atu2rVJSUvIsv2HDBnXv3l29evXSDz/8oI8//ljbt2/XM888Y6yONOJvUH6N75kzZyohIaFI6gQAAAAARcHiYimWy/WaNm2aevXqpWeeeUaRkZGaMWOGQkNDNXfu3DzLb9myRWFhYRowYICqVKmiu+++W88995x27NhR0EuaLxrxN1lAQIACAwOLuhoAAAAAcMtLT0/X6dOnHZb09PQ8y2ZkZCgpKUn33Xefw/r77rtPmzZtynOfpk2b6tdff9WqVatks9n0+++/65NPPtEDDzxw08/lEqdsxMfExGjAgAF66aWXFBQUpODgYMXHx9u3p6Wl6dlnn1W5cuXk7++ve++9V99++61Dxvjx41WuXDn5+fnpmWee0YgRI1SvXj379pycHI0dO1a33XabrFar6tWrp9WrV9u3V6lSRZJUv359WSwWxcTESMo9nH716tW6++67FRgYqNKlS+vBBx/UwYMHc53Tvn371LRpU3l6eqp27dpKTEy84jXYtGmTmjVrJi8vL4WGhmrAgAE6d+7ctV1AAAAAALgFTJgwQQEBAQ7LhAkT8iz7xx9/KDs7W+XLl3dYX758eR09ejTPfZo2baolS5aoS5cu8vDwUHBwsAIDAzV79uybfi6XOGUjXpIWLVokHx8fbd26VZMmTdLYsWO1Zs0a2Ww2PfDAAzp69KhWrVqlpKQkNWjQQC1bttSJEyck/TXxwGuvvaaJEycqKSlJlSpVyjU8YubMmZo6daqmTJmi7777Tm3atFH79u114MABSdK2bdskSV9++aVSU1P16aef5lnPc+fOafDgwdq+fbvW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911JUkZGhsaNG6dvv/1Wy5cv16FDh+wN9dDQUC1dulSStH//fqWmpmrmzJkOuT4+Ptq6dasmTZqksWPHas2aNQ7HHj16tDp06KA9e/aoZ8+eWrZsmV588UUNGTJE33//vZ577jk9/fTTWrdunSTJZrOpY8eOOnHihNavX681a9bo4MGD6tKli0PuwYMH9fnnn2v16tX617/+pQULFuiBBx7Qr7/+qvXr12vixIl69dVXtWXLFlOXFQAAAABQDJS458SHhoZq+vTpslgsioiI0J49ezR9+nT17t1bPXv2tJerWrWqZs2apSZNmujs2bPy9fVVUFCQJKlcuXIKDAx0yK1bt65Gjx4tSapevbrefPNNrV27Vq1bt7aX6datm8MxunXrptjYWPXt21eSNHjwYG3ZskVTpkxRixYt9OWXX+q7777ToUOHFBoaKkl6//33Vbt2bW3fvl2NGzeW9NcogAULFsjPz0+1atVSixYttH//fq1atUouLi6KiIjQxIkTlZiYqLvuuivP65Kenq709HSHdVmZOXJzt97IZQYAAAAAFIES1xN/1113yWL5v1kIo6KidODAAWVnZ2vXrl3q0KGDKleuLD8/P8XExEj6a0j71dStW9fhdUhIiH0o/iWNGjVyeJ2cnKzo6GiHddHR0UpOTrZvDw0NtTfgJalWrVoKDAy0l5GksLAw+fn52V+XL19etWrVkstlw0PKly+fqz6XmzBhggICAhyWrf+dfLXTBgAAAICrs1iK51IClbhGfH4uXryo++67T76+vlq8eLG2b9+uZcuWSfprmP3VuLu7O7y2WCzKyclxWOfj45NrP8vf3jg2m82+7vI/51cmv2NfS30uFxcXp7S0NIflzjbD8i0PAAAAACh+Slwj/u/3hW/ZskXVq1fXvn379Mcff+iNN97QPffco5o1a+bqufbw8JAkZWdn35S6REZGasOGDQ7rNm3apMjISEl/9bqnpKToyJEj9u179+5VWlqavczNYrVa5e/v77AwlB4AAAAAnEuJuyf+yJEjGjx4sJ577jnt3LlTs2fP1tSpU1WpUiV5eHho9uzZ6tOnj77//nuNGzfOYd/KlSvLYrFo5cqVateunby8vOTr63vDdRk2bJg6d+6sBg0aqGXLlvrss8/06aef6ssvv5QktWrVSnXr1tUTTzyhGTNmKCsrS3379lXz5s1zDc0HAAAAgGKrhM4EXxyVuCvdvXt3XbhwQU2aNNELL7yg/v3769lnn1XZsmWVkJCgjz/+WLVq1dIbb7yhKVOmOOxbsWJFjRkzRiNGjFD58uXVr1+/AtWlY8eOmjlzpiZPnqzatWtr/vz5Wrhwof1efIvFouXLl6tUqVJq1qyZWrVqpapVq+rDDz8s0HEBAAAAACWTxXbpIeq45bw074Kx7NBQTyO5zWscN5IrSZ4uF41ln8vxNpL7xbdBRnIl6UXfBUZyh3z/mJFcSWoXd6eR3PWzdxvJlaQGdc18VioEnDeSK0mRlh+M5Pps+9xIriQdvedJY9nnbbnnQ7kZ3v38xkeCXU2Dumayb6/wh5FcSUrPdr96oRvg42buu/9kupnr7O129bl8btSPxwON5EaW/9NIriQtXuNlLLteHTOf71NnzP33u1pIlpHc9CxzfX+e7vnP61QQNQKOXL3QDTp8roKR3Ja3m/l/QWE4nzCmqKuQJ+/Y0UVdhZuuxA2nBwAAAAAUshI6E3xxVOKG0wMAAAAAUFLRiAcAAAAAwEkwnB4AAAAAUCAWZqcvNFxpAAAAAACcBI14AAAAAACcBI+Yu4UNf9vcI+ZQOFxdzf0Ol51t5nEvFoMzl+Zkm/k6a96/npFcSfr6rd3Gsk2xmXlryMLPyg6c8fMN5Mfk+9kkU58VU9+jEt+lzm7is+YemWjahcWvF3UV8uT15MtFXYWbjo85AAAAAABOgkY8AAAAAABOgtnpAQAAAAAF42Lulkk4oiceAAAAAAAnQSP+BsXHx6tevXpFXQ0HFotFy5cvL+pqAAAAAAAMYTg9AAAAAKBALDwaodBwpZ1MZmZmUVcBAAAAAFBEnLoRn5OTo4kTJyo8PFxWq1WVKlXSa6+9psTERFksFp06dcpedvfu3bJYLDp8+LAkKSEhQYGBgVq+fLlq1KghT09PtW7dWkeOHLmuOsyfP1+hoaHy9vZWp06dHI6Zk5OjsWPH6rbbbpPValW9evW0evVqh/2HDx+uGjVqyNvbW1WrVtXIkSMdGuqXhu0vWLBAVatWldVqlc1m04EDB9SsWTN5enqqVq1aWrNmzXVfPwAAAACAc3Hq4fRxcXF65513NH36dN19991KTU3Vvn37rnn/8+fP67XXXtOiRYvk4eGhvn37qmvXrtq4ceM17f/TTz/po48+0meffabTp0+rV69eeuGFF7RkyRJJ0syZMzV16lTNnz9f9evX14IFC9S+fXv98MMPql69uiTJz89PCQkJqlChgvbs2aPevXvLz89PL730Uq7jLF26VK6ursrJydEjjzyiMmXKaMuWLTp9+rQGDhx47RcOAAAAAG4mZqcvNE7biD9z5oxmzpypN998Uz169JAkVatWTXfffbcSExOvKSMzM1Nvvvmm7rzzTknSokWLFBkZqW3btqlJkyZX3f/ixYtatGiRbrvtNknS7Nmz9cADD2jq1KkKDg7WlClTNHz4cHXt2lWSNHHiRK1bt04zZszQW2+9JUl69dVX7XlhYWEaMmSIPvzwQ4dGfEZGht5//32VLVtWkvTFF18oOTlZhw8fth/79ddfV9u2bfOta3p6utLT0x3WZWXmyM3detXzBAAAAAAUD047nD45OVnp6elq2bLlDWe4ubmpUaNG9tc1a9ZUYGCgkpOTr2n/SpUq2RvRkhQVFaWcnBzt379fp0+f1m+//abo6GiHfaKjox3yP/nkE919990KDg6Wr6+vRo4cqZSUFId9KleubG/AS3+de17HvpIJEyYoICDAYdmyevI1nScAAAAAoHhw2ka8l5dXvttcXP46LZvNZl+X34RwFkvuYR95rbsWl/a7fP+/Z9lsNvu6LVu2qGvXrmrbtq1WrlypXbt26ZVXXlFGRobDPj4+PrkyrrfOcXFxSktLc1juun/YtZ8cAAAAAOTH4lI8lxLIac+qevXq8vLy0tq1a3Ntu9RrnZqaal+3e/fuXOWysrK0Y8cO++v9+/fr1KlTqlmz5jXVISUlRb/99pv99ebNm+Xi4qIaNWrI399fFSpU0IYNGxz22bRpkyIjIyVJGzduVOXKlfXKK6+oUaNGql69un755ZerHrdWrVp5HvtKrFar/P39HRaG0gMAAACAc3Hae+I9PT01fPhwvfTSS/Lw8FB0dLSOHz+uH374Qd27d1doaKji4+M1fvx4HThwQFOnTs2V4e7urv79+2vWrFlyd3dXv379dNddd13T/fCX6tCjRw9NmTJFp0+f1oABA9S5c2cFBwdLkoYNG6bRo0erWrVqqlevnhYuXKjdu3fbJ74LDw9XSkqKPvjgAzVu3Fj/+c9/tGzZsqset1WrVoqIiFD37t01depUnT59Wq+88sp1XD0AAAAAgDNy2ka8JI0cOVJubm4aNWqUfvvtN4WEhKhPnz5yd3fXv/71Lz3//PO644471LhxY40fP16dOnVy2N/b21vDhw9Xt27d9Ouvv+ruu+/WggULrvn44eHheuSRR9SuXTudOHFC7dq105w5c+zbBwwYoNOnT2vIkCE6duyYatWqpRUrVthnpu/QoYMGDRqkfv36KT09XQ888IBGjhyp+Pj4Kx7XxcVFy5YtU69evdSkSROFhYVp1qxZuv/++6/94gEAAADAzXKDtyTj+llsed1gfQtISEjQwIEDHZ7rfqsZ/vaFoq4CCsjV1dwdMdnZOUZyb3TOiWuRk23m66x5/3pGciXp67d2G8s2xWbmrVFSb1u7Yc74+QbyY/L9bJKpz4qp71GJ71JnN/HZ/Of9Ku4ufpx75HNx4NlpSFFX4abjYw4AAAAAgJOgEZ+P2rVry9fXN8/l0j3tAAAAAABJLi7FcymBnPqe+IKIjY1VbGxsvttXrVqV72Ppypcvb6hWAAAAAADk75ZtxF9N5cqVi7oKAAAAAAA4oBEPAAAAACgYZlUsNFxpAAAAAACcBD3xtzCTj/qqHeFpJPfuij8ZyZUk15y850C4GTyyLxrJnbIuwkiuJNWt5W0k9/23k4zkSlKvFxoYyTX5GLhmL9Qzktt8RgcjuZL0831DjeRm5LgbyZWkEMuvxrKzXDyM5L6zoYqRXEmqUtnMI4zur7zXSK4knbEEGsktnZlqJFeSfnU183dYyvWkkVxJ2vBrNSO5jSr+ZiRXkj7YWMZY9j0NzPxX+Y8z5r7vygdkGMn19Ug3kmtSaY9TxrJPZvobSnbeR8yh8NCIBwAAAAAUjIu5DkI4Yjg9AAAAAABOgkY8AAAAAABOguH0AAAAAICCYXb6QsOVNshms+nZZ59VUFCQLBaLAgMDNXDgwKKuFgAAAADASdGIN2j16tVKSEjQypUrlZqaqjp16hR1lQAAAAAATozh9AYdPHhQISEhatq0qSTJzc385c7IyJCHh5nHHQEAAABAngw+vhqO6Ik3JDY2Vv3791dKSoosFovCwsJylTl58qS6d++uUqVKydvbW23bttWBAwccyixdulS1a9eW1WpVWFiYpk6d6rA9LCxM48ePV2xsrAICAtS7d2+TpwUAAAAAKEI04g2ZOXOmxo4dq9tuu02pqanavn17rjKxsbHasWOHVqxYoc2bN8tms6ldu3bKzMyUJCUlJalz587q2rWr9uzZo/j4eI0cOVIJCQkOOZMnT1adOnWUlJSkkSNHFsbpAQAAAACKAMPpDQkICJCfn59cXV0VHByca/uBAwe0YsUKbdy40T7cfsmSJQoNDdXy5cvVqVMnTZs2TS1btrQ3zGvUqKG9e/dq8uTJio2NtWfde++9Gjp0aKGcFwAAAADk4kL/cGHhSheR5ORkubm56c4777SvK126tCIiIpScnGwvEx0d7bBfdHS0Dhw4oOzsbPu6Ro0aXfV46enpOn36tMOSlZl+k84GAAAAAFAYaMQXEZvNlu96y/+fFOLyP19pPx8fn6seb8KECQoICHBYtnw++QZqDgAAAAAoKjTii0itWrWUlZWlrVu32tf9+eef+vHHHxUZGWkvs2HDBof9Nm3apBo1asjV1fW6jhcXF6e0tDSH5a62wwp+IgAAAABgsRTP5QbMmTNHVapUkaenpxo2bKhvvvnmiuXT09P1yiuvqHLlyrJarapWrZoWLFhwQ8e+FtwTX0SqV6+uDh06qHfv3po/f778/Pw0YsQIVaxYUR06dJAkDRkyRI0bN9a4cePUpUsXbd68WW+++abmzJlz3cezWq2yWq0O69zcL96UcwEAAACAkuDDDz/UwIEDNWfOHEVHR2v+/Plq27at9u7dq0qVKuW5T+fOnfX777/rvffeU3h4uI4dO6asrCxjdaQnvggtXLhQDRs21IMPPqioqCjZbDatWrVK7u7ukqQGDRroo48+0gcffKA6depo1KhRGjt2rMOkdgAAAACAm2PatGnq1auXnnnmGUVGRmrGjBkKDQ3V3Llz8yy/evVqrV+/XqtWrVKrVq0UFhamJk2a2CcvN4GeeIMGDhyogQMH2l8nJiY6bC9VqpT+8Y9/XDHj0Ucf1aOPPprv9sOHDxeghgAAAABwE1iKZ/9wenq60tMdJ/TOa5SyJGVkZCgpKUkjRoxwWH/fffdp06ZNeeavWLFCjRo10qRJk/T+++/Lx8dH7du317hx4+Tl5XXzTuQyxfNKAwAAAABQQHlN8D1hwoQ8y/7xxx/Kzs5W+fLlHdaXL19eR48ezXOfn3/+WRs2bND333+vZcuWacaMGfrkk0/0wgsv3PRzuYSeeAAAAABAiRQXF6fBgwc7rMurF/5yeT0h7O/rLsnJyZHFYtGSJUsUEBAg6a8h+Y899pjeeustI73xNOIBAAAAAAXjUjwHeec3dD4vZcqUkaura65e92PHjuXqnb8kJCREFStWtDfgJSkyMlI2m02//vqrqlevfuOVz0fxvNIAAAAAABQiDw8PNWzYUGvWrHFYv2bNmnwnqouOjtZvv/2ms2fP2tf9+OOPcnFx0W233WaknjTiAQAAAACQNHjwYL377rtasGCBkpOTNWjQIKWkpKhPnz6S/hqe3717d3v5bt26qXTp0nr66ae1d+9eff311xo2bJh69uxpbGI7htMDAAAAAAomn3vGnU2XLl30559/auzYsUpNTVWdOnW0atUqVa5cWZKUmpqqlJQUe3lfX1+tWbNG/fv3V6NGjVS6dGl17txZ48ePN1ZHGvG3MJvNZiw7wDvbSG7Z43uN5EqSxZZjLNv1/Gkzua41jeRKUrmADCO5F06fvXqhG1Qh4LyR3F0GBy01n9HBSO76gf82kitJ4fv6G8ktl/0/I7mSFPCbue8Om6u7mdycMCO5kuTmaia39NEfzARL8gkMMZLrnfK9kVxJyqhhpgem9NFkI7mSVMq3spHc4As/G8mVJDe3csayg31PGcnNygk0kitJZbzOGMn1dzXzfxmTyqYdNJbtHlDFUHLA1YvAuL59+6pv3755bktISMi1rmbNmrmG4JvEcHoAAAAAAJwEPfEAAAAAgIKx0D9cWLjSAAAAAAA4CRrxAAAAAAA4CYbTAwAAAAAKpoTMTu8M6Im/DrGxserYseM1lbXZbHr22WcVFBQki8Wi3bt3KyYmRgMHDjRaRwAAAABAyeX0jfgbaRgXRmN69erVSkhI0MqVK+3PFwQAAAAAoCAYTm/IwYMHFRISoqZNmxbqcTMyMuTh4VGoxwQAAABwi3Nx+v5hp+HUVzo2Nlbr16/XzJkzZbFYZLFYdPjwYa1fv15NmjSR1WpVSEiIRowYoaysrCvuk52drV69eqlKlSry8vJSRESEZs6cecP16t+/v1JSUmSxWBQWFpZnuZMnT6p79+4qVaqUvL291bZtWx04cMChzNKlS1W7dm1ZrVaFhYVp6tSpDtvDwsI0fvx4xcbGKiAgQL17976hOgMAAAAAij+nbsTPnDlTUVFR6t27t1JTU5Wamip3d3e1a9dOjRs31rfffqu5c+fqvffe0/jx4/PdJzQ0VDk5Obrtttv00Ucfae/evRo1apRefvllffTRRzdUr7Fjx+q2225Tamqqtm/fnme52NhY7dixQytWrNDmzZtls9nUrl07ZWZmSpKSkpLUuXNnde3aVXv27FF8fLxGjhyphIQEh5zJkyerTp06SkpK0siRI6+7vgAAAAAA5+DUw+kDAgLk4eEhb29vBQcHS5JeeeUVhYaG6s0335TFYlHNmjX122+/afjw4Ro1alSe+0iSq6urxowZY39dpUoVbdq0SR999JE6d+583fXy8/OTq6urwzEud+DAAa1YsUIbN260D7lfsmSJQkNDtXz5cnXq1EnTpk1Ty5Yt7Q3zGjVqaO/evZo8ebJiY2PtWffee6+GDh16xTqlp6crPT3dYV1WZo7c3K3XdW4AAAAA8Hc2ZqcvNE7dE5+X5ORkRUVFyXLZmyg6Olpnz57Vr7/+esV9582bp0aNGqls2bLy9fXVO++8o5SUFGP1dHNz05133mlfV7p0aUVERCg5OdleJjo62mG/6OhoHThwQNnZ2fZ1jRo1uurxJkyYoICAAIdly+rJN+lsAAAAAACFocQ14m02m0MD/tI6SbnWX+6jjz7SoEGD1LNnT33xxRfavXu3nn76aWVkZBirZ37rL9XzSudyOR8fn6seLy4uTmlpaQ7LXfcPu4GaAwAAAACKilMPp5ckDw8Ph17pWrVqaenSpQ4N4E2bNsnPz08VK1bMcx9J+uabb9S0aVP17dvXvu7gwYPG6l2rVi1lZWVp69at9uH0f/75p3788UdFRkbay2zYsMFhv02bNqlGjRpydXW9ruNZrVZZrY5D593cLxTgDAAAAADg/7OUuP7hYsvpr3RYWJi2bt2qw4cP648//lDfvn115MgR9e/fX/v27dO///1vjR49WoMHD5bL/3/swd/3ycnJUXh4uHbs2KH//ve/+vHHHzVy5Mh8J6S7GapXr64OHTqod+/e2rBhg7799ls9+eSTqlixojp06CBJGjJkiNauXatx48bpxx9/1KJFi/Tmm29e9f53AAAAAEDJ5PSN+KFDh8rV1VW1atVS2bJllZmZqVWrVmnbtm2644471KdPH/Xq1UuvvvpqvvukpKSoT58+euSRR9SlSxfdeeed+vPPPx165U1YuHChGjZsqAcffFBRUVGy2WxatWqV3N3dJUkNGjTQRx99pA8++EB16tTRqFGjNHbsWIdJ7QAAAAAAtw6nH05fo0YNbd682WFdWFiYtm3bdl37SH81qhcuXOiwbsKECfY///3RblcycOBADRw40GFdYmKiw+tSpUrpH//4xxVzHn30UT366KP5bj98+PA11wkAAAAAjGA4faHhSgMAAAAA4CRoxN+AlJQU+fr65ruYeiwdAAAAAODW5vTD6YtChQoVtHv37ituBwAAAIBbhe0Kj/PGzUUj/ga4ubkpPDy8qKsBAAAAALjFMJweAAAAAAAnQU88AAAAAKBgmJ2+0NCIv4UFBHgYyz6XbuZDfKpsVSO5khR44mdj2f+rcreRXM//mfsIh/v9aiS3Uu1qRnIlKdLyg5HclTm3G8mVpJ/vG2okN3xffyO5kvRTzVZGcqOS3jWSK8nofyzOlDXznk7bcdFI7l+sRlJ/r1DfSK4kWWw5RnLPRLQwkitJpxVoJDenfB0juZL0569m/l1x879gJFeSjh8/byw7+ffSRnLTzpq7d7iMt7uR3CPpwUZyJamU51kjueVzsozkStKJrCAjueb+p4uShJ9LAAAAAABwEvTEAwAAAAAKhtnpCw098QAAAAAAOAka8QAAAAAAOIkS2YiPiYnRwIEDb3j/xMREWSwWnTp16qbV6Wri4+NVr169QjseAAAAANw0Li7FcymBSuZZOaGhQ4dq7dq1RV0NAAAAAEAxxsR2xYSvr698fX2LuhoAAAAAgGKsxPbEZ2VlqV+/fgoMDFTp0qX16quvymazSZIWL16sRo0ayc/PT8HBwerWrZuOHTt2xbyNGzeqefPm8vb2VqlSpdSmTRudPHlSkpSenq4BAwaoXLly8vT01N13363t27fb9700PH/t2rVq1KiRvL291bRpU+3fv99eJq/h9AsXLlRkZKQ8PT1Vs2ZNzZkzx74tIyND/fr1U0hIiDw9PRUWFqYJEyYU9LIBAAAAwHWzWSzFcimJSmwjftGiRXJzc9PWrVs1a9YsTZ8+Xe+++66kvxrA48aN07fffqvly5fr0KFDio2NzTdr9+7datmypWrXrq3Nmzdrw4YNeuihh5SdnS1Jeumll7R06VItWrRIO3fuVHh4uNq0aaMTJ0445LzyyiuaOnWqduzYITc3N/Xs2TPfY77zzjt65ZVX9Nprryk5OVmvv/66Ro4cqUWLFkmSZs2apRUrVuijjz7S/v37tXjxYoWFhRXsogEAAAAAirUSO5w+NDRU06dPl8ViUUREhPbs2aPp06erd+/eDo3nqlWratasWWrSpInOnj2b55D2SZMmqVGjRg494bVr15YknTt3TnPnzlVCQoLatm0r6a8G+Jo1a/Tee+9p2LBh9n1ee+01NW/eXJI0YsQIPfDAA7p48aI8PT1zHXPcuHGaOnWqHnnkEUlSlSpVtHfvXs2fP189evRQSkqKqlevrrvvvlsWi0WVK1e+4vVIT09Xenq6w7qsTDe5uVuvuB8AAAAAoPgosT3xd911lyyXDZ+IiorSgQMHlJ2drV27dqlDhw6qXLmy/Pz8FBMTI0lKSUnJM+tST3xeDh48qMzMTEVHR9vXubu7q0mTJkpOTnYoW7duXfufQ0JCJCnPYfzHjx/XkSNH1KtXL/u98r6+vho/frwOHjwoSYqNjdXu3bsVERGhAQMG6Isvvrji9ZgwYYICAgIclvXL37jiPgAAAABwTSwuxXMpgUpsT3x+Ll68qPvuu0/33XefFi9erLJlyyolJUVt2rRRRkZGnvt4eXnlm3fpPnvL3+63sNlsuda5u7vb/3xpW05OTq7MS+veeecd3XnnnQ7bXF1dJUkNGjTQoUOH9Pnnn+vLL79U586d1apVK33yySd51jMuLk6DBw92WDdjxS331w8AAAAATq1k/jQhacuWLbleV69eXfv27dMff/yhN954Q/fcc49q1qx51Unt6tatm+/j38LDw+Xh4aENGzbY12VmZmrHjh2KjIy8obqXL19eFStW1M8//6zw8HCHpUqVKvZy/v7+6tKli9555x19+OGHWrp0aa778C+xWq3y9/d3WBhKDwAAAADOpcR2xR45ckSDBw/Wc889p507d2r27NmaOnWqKlWqJA8PD82ePVt9+vTR999/r3Hjxl0xKy4uTrfffrv69u2rPn36yMPDQ+vWrVOnTp1UpkwZPf/88xo2bJiCgoJUqVIlTZo0SefPn1evXr1uuP7x8fEaMGCA/P391bZtW6Wnp2vHjh06efKkBg8erOnTpyskJET16tWTi4uLPv74YwUHByswMPCGjwkAAAAAN8JWQoeuF0clthHfvXt3XbhwQU2aNJGrq6v69++vZ599VhaLRQkJCXr55Zc1a9YsNWjQQFOmTFH79u3zzapRo4a++OILvfzyy2rSpIm8vLx055136vHHH5ckvfHGG8rJydFTTz2lM2fOqFGjRvrvf/+rUqVK3XD9n3nmGXl7e2vy5Ml66aWX5OPjo9tvv10DBw6U9Ndz5SdOnKgDBw7I1dVVjRs31qpVq+TiwocHAAAAAEoqi+3STd245bz+Ybax7Cq3mfkx4Z6yPxjJlaTAEz8by/69XB0juf/YEGokV5Keiv7VSO6od9yvXugGzez+m5HcyV/fbiRXkp5secZIrtUl/eqFbtBPNVsZyY1KetdIriR5nTDzfpak0+VrGMkd93m4kVxJalg/wEhuTKWfjORKksWWew6Zm5Irc/8NOq1AI7n+OmUkV5LW/RphJPcR/zVGciXpla/vvHqhGxTVyM9IbtpZc8+urlf5tJHci1nm/v0u5XnWSG61tCQjuZK038/M+65RxI13Aha1s1tWFHUV8uR7V/6dtc6qxPbEAwAAAAAKicXcj1NwxNhrAAAAAACcBI14AAAAAACcBMPpAQAAAAAFwuz0hYcrDQAAAACAk6ARDwAAAACAk2A4/S0sM9PM43r+Yub3IdecLCO5kpTuW8ZYtk9GmplcnzAjuZJ0209fGcmtUPlxI7mS5LPtPSO5Fhdzj5jLyDHzyJ5y2f8zkiuZexTc5obPGMmVpOhtc41lu9jMPK7T3cPVSK4kVQzKMJJrzTpvJFeSMlw9jeR6p58ykitJZ6xmHuVn6j0nSUG+ZrLT/CoayZUkL0+Djz7zMfP/jgyDj2szxcPV3PsuK8dMkyTbzcz3hiS5upi7Hk6L2ekLDT3xAAAAAAA4CRrxAAAAAAA4CYbTAwAAAAAKhtnpCw1XGgAAAAAAJ0EjHgAAAAAAJ0EjvgSwWCxavnx5UVcDAAAAwC3KZrEUy6UkohFfhDIyzDziBwAAAABQMtGIL0QxMTHq16+fBg8erDJlyqh169bau3ev2rVrJ19fX5UvX15PPfWU/vjjD4d9BgwYoJdeeklBQUEKDg5WfHy8fXtYWJgk6eGHH5bFYrG/BgAAAACUPDTiC9miRYvk5uamjRs36o033lDz5s1Vr1497dixQ6tXr9bvv/+uzp0759rHx8dHW7du1aRJkzR27FitWbNGkrR9+3ZJ0sKFC5Wammp/DQAAAACFxuJSPJcSiEfMFbLw8HBNmjRJkjRq1Cg1aNBAr7/+un37ggULFBoaqh9//FE1atSQJNWtW1ejR4+WJFWvXl1vvvmm1q5dq9atW6ts2bKSpMDAQAUHBxfy2QAAAAAAChON+ELWqFEj+5+TkpK0bt06+fr65ip38OBBh0b85UJCQnTs2LHrOm56errS09Md1mVlusjN3XpdOQAAAACAokMjvpD5+PjY/5yTk6OHHnpIEydOzFUuJCTE/md3d3eHbRaLRTk5Odd13AkTJmjMmDEO65o//KpaPDLqunIAAAAA4O9sKpkzwRdHNOKLUIMGDbR06VKFhYXJze3G/yrc3d2VnZ19xTJxcXEaPHiww7rJS0vmPSIAAAAAUFLRiitCL7zwgk6cOKHHH39c27Zt088//6wvvvhCPXv2vGqj/HJhYWFau3atjh49qpMnT+ZZxmq1yt/f32FhKD0AAAAAOBca8UWoQoUK2rhxo7Kzs9WmTRvVqVNHL774ogICAuTicu1/NVOnTtWaNWsUGhqq+vXrG6wxAAAAAORms7gUy6UkYjh9IUpMTMy1rnr16vr000+va5/ly5c7vH7ooYf00EMPFbB2AAAAAIDirmT+NAEAAAAAQAlETzwAAAAAoGBK6ND14ogrDQAAAACAk6ARDwAAAACAk2A4PQAAAACgQGwWS1FX4ZZBTzwAAAAAAE6CnvhbWE6OuexSPplmcn/eZiRXknaPeddYdp2ZrxrJPXWqlpFcSdpXt72R3G//kWwkV5KOjn3STPBaM7GSFGL51UhuwG97jeRKMjZxTfS2uUZyJWljk+eNZbf8oI+R3IsXahjJlaQ/z/oYyQ08vd9IriRZsjKM5NpcXI3kSlLFwItGcr1++d5IriRdLFvTSK7fp3OM5ErSyewxxrJtNn8juS4GOyzLexw3kpshq5FcSSpz4YiR3OwV/zSSK0llHh9oKtlQLkoSeuIBAAAAAHAS9MQDAAAAAArExiPmCg1XGgAAAAAAJ0EjHgAAAAAAJ8FwegAAAABAwfCIuUJDTzwAAAAAAE6CRnwhio2NVceOHfPcFhYWphkzZji8tlgsDsttt92m+Pj4XOv/vhw+fLhQzgcAAAAAULgYTl+MjR07Vr1797a/dnV1lZeXl/r0+b9nEjdu3FjPPvusQ7myZcsWaj0BAAAA3NqYnb7w0Igvxvz8/BQcHJxrva+vr/3Prq6u+ZYDAAAAAJQs/FwCAAAAAICToBFfjA0fPly+vr72ZdasWTeclZ6ertOnTzssWZnpN7G2AAAAAG5VNlmK5VIS0YgvxoYNG6bdu3fbl+7du99w1oQJExQQEOCwbFg58SbWFgAAAABgGvfEF2NlypRReHj4TcmKi4vT4MGDHdZN/JjfcAAAAADAmdCIv0VYrVZZrVaHdW7umUVUGwAAAAAlCbPTFx4a8YUsLS1Nu3fvdlgXFBRUNJUBAAAAADgVGvGFLDExUfXr13dY16NHjyKqDQAAAADAmdCIL0QJCQlKSEi4prKHDx++qeUAAAAAwBhLyZwJvjjixgUAAAAAAJwEjXgAAAAAAJwEw+kBAAAAAAVio3+40HClAQAAAABwEjTiAQAAAABwEgynBwAAAAAUiI3Z6QsNjfhbmJu7uQ+al3umkdwdcfOM5EpSo4l9jWVnbPrKTHBAGzO5kjJz3I1lm3Le5lPUVbhuWS4eRnJtrub+/s6UrWYk18WWbSRXklp+0MdY9tquZr6Xguab+04y9f+s7J1bzARLcg+tZCT3/Pc/GMmVJK+YVsayTfF0txnJ9YhqZiRXkoL2eRvL9nDLMZJboVS6kVxJyjb033v/rBNGciXJIjPvO5+6dYzkSlJ6TpaxbOBqGE4PAAAAAICToCceAAAAAFAgNgv9w4WFKw0AAAAAgJOgEQ8AAAAAgJNgOD0AAAAAoEBsYnb6wkJPfCE5evSoXnzxRYWHh8vT01Ply5fX3Xffrblz5+ree+9Vmza5ZxmfM2eOAgIClJKSosTERFksFpUqVUoXL150KLdt2zZZLBZZeKwDAAAAAJRoNOILwc8//6z69evriy++0Ouvv65du3bpyy+/1KBBg7Ry5Ur16NFDW7du1fz58+37HDp0SMOHD9fMmTNVqdL/PVbHz89Py5Ytc8hfsGCBQxkAAAAAQMnEcPpC0LdvX7m5uWnHjh3y8fm/51jffvvtevTRR2Wz/fVszH79+um+++5TWFiYevXqpZYtWyo2NtYhq0ePHlqwYIEef/xxSdKFCxf0wQcfaMCAARo3blyhnRMAAAAAXMLs9IWHK23Yn3/+qS+++EIvvPCCQwP+chaLRT169FDLli319NNP680339T333+vt99+O1fZp556St98841SUlIkSUuXLlVYWJgaNGhg9DwAAAAAAEWPRrxhP/30k2w2myIiIhzWlylTRr6+vvL19dXw4cMlSW+//bb27t2rgQMHav78+SpXrlyuvHLlyqlt27ZKSEiQ9NdQ+p49e161Hunp6Tp9+rTDkpWZXvATBAAAAAAUGhrxheTvk85t27ZNu3fvVu3atZWe/ldjuly5cnr22WcVGRmphx9+ON+snj17KiEhQT///LM2b96sJ5544qrHnzBhggICAhyWr/89sWAnBQAAAACSbBZLsVxKIhrxhoWHh8tisWjfvn0O66tWrarw8HB5eXk5rHdzc5Ob25WnKmjXrp0uXryoXr166aGHHlLp0qWvWo+4uDilpaU5LM06DL/+EwIAAAAAFBka8YaVLl1arVu31ptvvqlz587dlExXV1c99dRTSkxMvKah9JJktVrl7+/vsLi5W29KfQAAAAAAhYNGfCGYM2eOsrKy1KhRI3344YdKTk7W/v37tXjxYu3bt0+urq7XnTlu3DgdP348z+fLAwAAAEBhsslSLJeSiEfMFYJq1app165dev311xUXF6dff/1VVqtVtWrV0tChQ9W3b9/rzvTw8FCZMmUM1BYAAAAAUFzRiC8kISEhmj17tmbPnn3FcvHx8YqPj8+1PiYmxv48+bx07NjxitsBAAAAAM6PRjwAAAAAoEBsFu7ULixcaQAAAAAAnASNeAAAAAAAnATD6QEAAAAABVJSZ4IvjuiJBwAAAADg/5szZ46qVKkiT09PNWzYUN9888017bdx40a5ubmpXr16RutHIx4AAAAAAEkffvihBg4cqFdeeUW7du3SPffco7Zt2yolJeWK+6Wlpal79+5q2bKl8TpabDyX7JY1dO55Y9lZWTlGcn183I3kSlLaqYvGsgODvIzkmqyzm5uZ3/jc3VyN5EpSRma2kVxvb3PvOxdXM0PPbDnmvtpNve/cPcy9Ny5eyDKWHVTazOe76XN1jeRK0u739xrJPXMm00iuJPn7m/kcnr9g5ntDMvc5NPX9LEnZhup8/OhZI7mS1O0hT2PZ/91i5nup0e3m/l3ZsjPdSK6Pr7m7cE39W5h2KsNIrklTnvcu6ircsF9+2l/UVchT5fCI6yp/5513qkGDBpo7d659XWRkpDp27KgJEybku1/Xrl1VvXp1ubq6avny5dq9e/eNVvmq6IkHAAAAAJRI6enpOn36tMOSnp73j10ZGRlKSkrSfffd57D+vvvu06ZNm/I9xsKFC3Xw4EGNHj36ptY9PzTiAQAAAAAl0oQJExQQEOCw5Nej/scffyg7O1vly5d3WF++fHkdPXo0z30OHDigESNGaMmSJXJzK5x545mdHgAAAABQIMV1dvq4uDgNHjzYYZ3Var3iPhaL47nYbLZc6yQpOztb3bp105gxY1SjRo2CV/Ya0YgHAAAAAJRIVqv1qo32S8qUKSNXV9dcve7Hjh3L1TsvSWfOnNGOHTu0a9cu9evXT5KUk5Mjm80mNzc3ffHFF7r33nsLfhJ/w3B6AAAAAMAtz8PDQw0bNtSaNWsc1q9Zs0ZNmzbNVd7f31979uzR7t277UufPn0UERGh3bt368477zRSzxLTiI+NjVXHjh3tf7ZYLHrjjTccyixfvtw+DOJSmSstVyp3//3323PDwsLs6728vFSzZk1NnjxZl0/8f/jwYVksFpUrV05nzpxxqFe9evUUHx9vfx0TE5PnMfv06aOEhISr1jsxMfEmXlkAAAAAuDKbxaVYLtdr8ODBevfdd7VgwQIlJydr0KBBSklJUZ8+fST9NTy/e/fukiQXFxfVqVPHYSlXrpw8PT1Vp04d+fj43NRrfEmJHU7v6empiRMn6rnnnlOpUqVybZ85c6ZDIz8kJEQLFy50aJxfcv/992vhwoUO6/4+JGPs2LHq3bu3Ll68qC+//FLPP/+8/P399dxzzzmUO3PmjKZMmaIxY8Zcsf69e/fW2LFjHdZ5e3vL3d3doY6PPPKI6tSp41A2KCjoitkAAAAAgNy6dOmiP//8U2PHjlVqaqrq1KmjVatWqXLlypKk1NTUqz4z3rQS24hv1aqVfvrpJ02YMEGTJk3Ktf3SzISXCwwMVHBwcK6yVqs1z/WX8/Pzs5d55plnNHfuXH3xxRe5GvH9+/fXtGnT9MILL6hcuXL55nl7e+d7TC+v/3smsYeHxxXLAgAAAACuXd++fdW3b988tyUkJFxx3/j4eIdR1iaUmOH0f+fq6qrXX39ds2fP1q+//lpox7XZbEpMTFRycrLc3d1zbX/88ccVHh6eq5cdAAAAAJyVTZZiuZREJbYRL0kPP/yw6tWrp9GjRxcoZ+XKlfL19XVYxo0b51Bm+PDh8vX1ldVqVYsWLWSz2TRgwIBcWZfu1X/77bd18ODBfI85Z86cXMdctGhRgc4DAAAAAODcSuxw+ksmTpyoe++9V0OGDLnhjBYtWmju3LkO6/5+3/mwYcMUGxur48eP65VXXtG9996b5wyGktSmTRvdfffdGjlypP75z3/mWeaJJ57QK6+84rDuSsPvryY9PV3p6ekO67Iys+Xmfm2PWwAAAAAAFL0S34hv1qyZ2rRpo5dfflmxsbE3lOHj46Pw8PArlilTpozCw8MVHh6upUuXKjw8XHfddZdatWqVZ/k33nhDUVFRGjZsWJ7bAwICrnrM6zFhwoRck+lFtXtZTR98JZ89AAAAAODa2Cwlc+h6cVSih9Nf8sYbb+izzz7Tpk2bCuV4pUqVUv/+/TV06FCHx8xdrkmTJnrkkUc0YsSIQqlTXFyc0tLSHJYmbYYWyrEBAAAAADdHie+Jl6Tbb79dTzzxhGbPnn1D+6enp+vo0aMO69zc3FSmTJl893nhhRc0ceJELV26VI899lieZV577TXVrl1bbm65/xrOnz+f65hWqzXPx+VdC6vVmuuxeG7u528oCwAAAABQNG6JnnhJGjduXL694lezevVqhYSEOCx33333FfcpW7asnnrqKcXHxysnJyfPMjVq1FDPnj118eLFXNveeeedXMd8/PHHb6j+AAAAAGCSzWYplktJZLHdaMsWTm/oXHM98VlZef9wUVA+Prkf23ezpJ3K/WPKzRIY5GUk12Sd3dzM/Mbn7uZqJFeSMjKzjeR6e5t737m4mvnHxZZj7qvd1PvO3cPce+PihSxj2UGlzXy+mz5X10iuJO1+f6+R3DNnMo3kSpK/v5nP4fkLZr43JHOfQ1Pfz5KUbajOx4+eNZIrSd0e8jSW/d8tZr6XGt1u7t+VLTvTr17oBvj4mhvAa+rfwrRTGUZyTZryvHdRV+GG/XTwUFFXIU/h1aoUdRVuulumJx4AAAAAAGd3S9wTDwAAAAAwx0b/cKHhSgMAAAAA4CRoxAMAAAAA4CQYTg8AAAAAKBCbSuZM8MURPfEAAAAAADgJeuJvYSYfURMSYuaRSyFljMRKkrJzrMayre5mHrm3e6+5OteoZiZ7774LRnIlqUFdXyO5P+w3V+cqlc18Vgw+yU+SmfdGxSBzjwL686yPsWyLoY4HU4+Bk6R6T9Uykntm/T4juZJkdTPzPZptM/dfoTPnzfw762U19whJU9f5bNUgI7mS9FWSuUcb1gw38yi4Q7+Z+zuMjHC+f1c8Pcy876xu5v6fdOKs0X9ogSuiEQ8AAAAAKBCG0xcehtMDAAAAAOAkaMQDAAAAAOAkGE4PAAAAACgQhtMXHnrigf/H3n1HRXU07gN/Lm0pS1FRAUUQERHU15LYo2DsvcQS1ARbNNbEjklsUYlGYzcaFdEY66sSNb52scReEBOxa9QodkBBYIH5/eHP/boCKrs7wOLzOeeeI/fOPju7bps7c2eIiIiIiIhMBBvxRERERERERCaCjfh86vDhwzA3N0fTpk0zHUtNTcW0adPwn//8B7a2tnB2dkadOnWwbNkyaDTyllkhIiIiIiLKioCSL7eCiNfE51NhYWEYNGgQlixZgps3b6JUqVIAXjTgmzRpgrNnz+L7779HnTp14ODggKNHj2L69OmoUqUKKleunLeVJyIiIiIiIinYiM+HEhMTsW7dOpw4cQKxsbEIDw/H2LFjAQCzZs3CgQMHcPLkSVSpUkV7Gy8vL3Ts2BGpqal5VW0iIiIiIiKSjMPp86G1a9eiXLlyKFeuHLp164Zly5ZBCAEA+O2339CwYUOdBvxLlpaWsLOzy+3qEhERERHRe04IJV9uBREb8fnQ0qVL0a1bNwBA06ZN8ezZM+zZswcAcPnyZfj6+uY4MyUlBQkJCTpbmibFqPUmIiIiIiIiudiIz2cuXryI48ePo0uXLgAACwsLdO7cGWFhYQAAIQQUJednlEJDQ+Ho6KizHf3fj0atOxEREREREcnFa+LzmaVLlyItLQ0lSpTQ7hNCwNLSEk+ePIGPjw9iYmJynBsSEoKhQ4fq7Ju4UhhcXyIiIiIiooI6E3x+xEZ8PpKWloYVK1ZgxowZaNy4sc6xDh064LfffkNQUBDGjBmDM2fOZLouPi0tDSkpKVleF69SqaBSqXT2WVgmG/9BEBERERERkTRsxOcjW7duxZMnT9CrVy84OjrqHPvkk0+wdOlSHD16FH/88Qc+/vhjfP/996hbty7s7e1x8uRJTJ06FUuXLuUSc0RERERERAUUG/H5yNKlS9GwYcNMDXjgRU/8lClT8Pfff2PXrl2YOXMmFi1ahOHDh8PW1hbly5fH4MGDUaFChTyoORERERERvc84nD73sBGfj2zZsiXbY1WrVtUuMwcAo0ePxujRo3OjWkRERERERJRPcHZ6IiIiIiIiIhPBnngiIiIiIiIyCIfT5x72xBMRERERERGZCDbiiYiIiIiIiEwEh9MTERERERGRQYTgcPrcwp54IiIiIiIiIhPBnvj3mI2NubRsf0+NlNxau0dIyQUAyw9rSctOiTwgJTeq2EwpuQBQrniClNz//nZbSi4AfPpxMSm5f1+0k5ILAE09zkvJLRL7t5RcALjnVkVKriotSUouADglXJSWnX76qJTcybaTpeQCwNP9F6Tk2tf3lZILAIGRU6Tkag5HSskFAJWnp5zgwkXl5AI45vKJlNxASznvEwD4Ma2OtOwKro+k5D50speSCwBVLKOk5FonPZaSCwBxjqWk5Ba5HyMlFwAyrC0lJbeWlEsFCRvxREREREREZJAMzk6fazicnoiIiIiIiMhEsBFPREREREREZCI4nJ6IiIiIiIgMIjicPtewJ56IiIiIiIjIRLARb2SxsbEYNGgQvLy8oFKp4O7ujlatWmHPnj0AAE9PT8yaNSvL2yqKgoiIiEz7v/rqKwQEBGj/Dg4OhqIo2q1IkSJo2rQpoqOjJTwiIiIiIiIiyi/YiDeiGzduoFq1ati7dy+mTZuGc+fOYfv27QgMDMSAAQOMel9NmzbF3bt3cffuXezZswcWFhZo2bKlUe+DiIiIiIjoXQih5MutIOI18UbUv39/KIqC48ePw87u/9aV9vf3R8+ePY16XyqVCi4uLgAAFxcXjBo1CvXq1cODBw9QtKi89WOJiIiIiIgo77An3kgeP36M7du3Y8CAAToN+JecnJyk3fezZ8/w22+/wdvbG0WKFJF2P0RERERERJS32BNvJFeuXIEQAr6+vrlyf1u3boVarQYAJCYmwtXVFVu3boWZWdbnZVJSUpCSkqKzL01jBgtLlfS6EhERERFRwcbZ6XMPe+KNRAgB4MXkdLkhMDAQUVFRiIqKwrFjx9C4cWM0a9YM//zzT5blQ0ND4ejoqLMd3DI1V+pKRERERERExsFGvJGULVsWiqIgJiZG7wx7e3vEx8dn2h8XFwdHR0edfXZ2dvD29oa3tzeqV6+OpUuXIjExEYsXL84yOyQkBPHx8TrbR61G6V1XIiIiIiIiyn1sxBtJ4cKF0aRJE8yfPx+JiYmZjsfFxb01w9fXFydOnNDZJ4TAqVOnUK5cuTfeVlEUmJmZ4fnz51keV6lUcHBw0Nk4lJ6IiIiIiIwhr2eh5+z0pJcFCxagdu3aqF69OiZOnIhKlSohLS0Nu3btws8//6ztpf/3338RFRWlc9tSpUph+PDh+Pzzz+Hr64vGjRvj+fPn+OWXX3D16tVMS9SlpKQgNjYWAPDkyRPMmzcPz549Q6tWrXLlsRIREREREVHuYyPeiEqXLo3Tp09j8uTJGDZsGO7evYuiRYuiWrVq+Pnnn7Xlpk+fjunTp+vcdtmyZQgODoYQAtOnT8c333wDa2trVKlSBQcPHoSHh4dO+e3bt8PV1RXAi2H4vr6+WL9+PQICAqQ/TiIiIiIiIsobbMQbmaurK+bNm4d58+ZlefzGjRtvvH3nzp3RuXPnN5YJDw9HeHi4njUkIiIiIiIyLs5On3t4TTwRERERERGRiWAjnoiIiIiIiMhEcDg9ERERERERGaSgzgSfH7EnnoiIiIiIiMhEsBFPREREREREZCI4nJ6IiIiIiIgMkpHXFXiPsBH/HrOykjcQIy1DSMlVVaosJRcANLYO0rJVdQKk5Jpdk3ftUUq6pZRcKxsrKbmAvDrL9FRxkpJr5+QqJRcAFCHnazrV3FpKLgAoaanSsi3dS0nJddDIez2rLOT8HwZGTpGSCwD7AsZIyf1460gpuQDwtGQFKbnqB9ek5AJA/HOVlFxhaS4lFwDMzeV9Fz56rpaSm5Yur85x6uJSclWW9lJyAcAu5YmUXLPkRCm5APCo1AdScuW84qig4XB6IiIiIiIiIhPBnngiIiIiIiIyCGenzz3siSciIiIiIiIyEWzEExEREREREZkIDqcnIiIiIiIigwhwOH1uMdme+ODgYLRt21b7b0VR8MMPP+iUiYiIgKIoOmXetL2pXNOmTbW5np6e2v02Njbw9fXFjz/+CCF0Z2Q/c+YMOnbsiOLFi8Pa2ho+Pj7o06cPLl26pFNu+fLlqF69Ouzs7GBvb4969eph69atOmUiIyOhKAoKFSqE5ORknWPHjx/XeQxERERERERUMJlsI/511tbWmDp1Kp48yXqJitmzZ+Pu3bvaDQCWLVuWaR8ANG3aVGf/3bt3sXr1ap28iRMn4u7du4iJicHw4cMxZswY/PLLL9rjW7duRc2aNZGSkoLffvsNMTEx+PXXX+Ho6IjvvvtOW2748OHo27cvOnXqhLNnz+L48eP46KOP0KZNG8ybNy/T47C3t8emTZt09oWFhaFUKTlLHBEREREREVH+UWCG0zds2BBXrlxBaGgopk2blum4o6MjHB0ddfY5OTnBxcUlU1mVSpXl/lfZ29try/Tu3Rs///wzdu7cib59+yIpKQk9evRA8+bNdRrcpUuXRo0aNRAXFwcAOHr0KGbMmIE5c+Zg0KBB2nKTJ09GcnIyhg4dijZt2sDd3V177PPPP0dYWBg+/fRTAMDz58+xZs0aDB48GN9///1bniUiIiIiIiLj4+z0uafA9MSbm5tjypQpmDt3Lm7fvp1r9yuEQGRkJGJiYmBpaQkA2LFjBx4+fIiRI0dmeRsnJycAwOrVq6FWq9G3b99MZYYNGwaNRoMNGzbo7O/evTsOHjyImzdvAgA2bNgAT09PVK1a1YiPioiIiIiIiPKjAtOIB4B27dqhcuXKGDdunEE5W7duhVqt1tle7+UeNWoU1Go1VCoVAgMDIYTA4MGDAQCXL18GAPj6+r7xfi5duoQyZcrAysoq0zE3Nzc4Ojpmun6+WLFiaNasGcLDwwG8GErfs2dPfR8qERERERERmZACM5z+palTp6JBgwYYNmyY3hmBgYH4+eefdfYVLlxY5+8RI0YgODgYDx48wDfffIMGDRqgdu3aAJBpgjt9CSGynKyuZ8+eGDJkCLp164YjR45g/fr1OHjw4BuzUlJSkJKSorMvTWMBC0uVUepKRERERETvL85On3sKVE88ANSrVw9NmjTBmDFj9M6ws7ODt7e3zvZ6I97Z2Rne3t6oVasWNmzYgJkzZ2L37t0AAB8fHwDAhQsX3ng/Pj4+uHr1KlJTUzMdu3PnDhISElC2bNlMx5o3b47k5GT06tULrVq1QpEiRd76mEJDQ7XzArzcIiN+eOvtiIiIiIiIKP8ocI14APjhhx+wZcsWHD58OFfur1ChQhg0aBCGDx8OIQQaN24MZ2fnLCfYA6Cd2K5Lly549uwZFi1alKnM9OnTYWlpiQ4dOmQ6Zm5uju7duyMyMvKdh9KHhIQgPj5eZwtoO/rdHyQRERERERHluQI3nB4AKlasiK5du2Lu3Ll63T4lJQWxsbE6+ywsLODs7JztbQYMGICpU6diw4YN+OSTT7BkyRJ07NgRrVu3xuDBg+Ht7Y2HDx9i3bp1uHnzJtasWYNatWphyJAhGDFiBFJTU9G2bVtoNBqsXLkSs2fPxqxZs3Rmpn/V999/jxEjRrxTLzzwYsZ9lUp36LyFZfo73ZaIiIiIiOhNMoxzRTG9gwLZEw+8aOTqe2369u3b4erqqrPVrVv3jbcpWrQounfvjvHjxyMjIwNt2rTB4cOHYWlpiaCgIPj6+uLTTz9FfHw8Jk2apL3drFmzsGDBAqxZswYVK1ZEtWrVsH//fkREROgsO/c6KysrODs7Z3nNPBERERERERVMJtsT/3J29tf//ZKHhweSk5OzvX12Dfzw8PAs815148aNLPf/8ssvOn9/8MEHmZaIy0rPnj3fOiw+ICDgjScl2rZta7QJ9YiIiIiIiCh/MtlGPBEREREREeUPnJ0+9xTY4fREREREREREBQ0b8UREREREREQmgsPpiYiIiIiIyCBCcDh9bmFPPBEREREREZGJYCOeiIiIiIiIyERwOP17LC1d3pJ01hbpUnJTz5+TkgsASu1i0rJPD/pBSq4Y0kZKLgDYWqRKyX2ekCQlFwDsLLJfVtIwVpJygSKau1JybW/+JSUXAJ6WC5SSa5sSJyUXAISZubTspL/+lpNbSs7nKACkCzlf/5rDkVJyAeDjrSOl5O5pOU1KLgAE7A+VkqskxkvJBQALhwwpuUqGvNezTFaSfs/YWcn5jgWAdMj5vLPRPJWSCwDpZnK+ZzMs5H1/W2ueScs2VVztOvewJ56IiIiIiIjIRLART0RERERERGQiOJyeiIiIiIiIDJIBzk6fW9gTT0RERERERGQi2IgnIiIiIiIiMhEcTk9EREREREQGEYLD6XMLe+KNIDg4GIqiQFEUWFpawsvLC8OHD0diYqK2zPLly1G9enXY2dnB3t4e9erVw9atWzNlpaenY+bMmahUqRKsra3h5OSEZs2a4c8//9QpFx4eDicnJ9kPjYiIiIiIiPIRNuKNpGnTprh79y6uXbuGSZMmYcGCBRg+fDgAYPjw4ejbty86deqEs2fP4vjx4/joo4/Qpk0bzJs3T5shhECXLl0wceJEDB48GDExMdi/fz/c3d0REBCAiIiIPHp0RERERERElB9wOL2RqFQquLi4AACCgoKwb98+RERE4PPPP8eMGTMwZ84cDBo0SFt+8uTJSE5OxtChQ9GmTRu4u7tj3bp1+O9//4vNmzejVatW2rK//PILHj16hN69e6NRo0aws7PL9cdHRERERESUHSHyugbvD/bES2JjYwONRoPVq1dDrVajb9++mcoMGzYMGo0GGzZsAACsWrUKPj4+Og34V8s+evQIu3btkl53IiIiIiIiyp/YEy/B8ePHsWrVKnz88ce4dOkSypQpAysrq0zl3Nzc4OjoiEuXLgEALl26hPLly2eZ+XL/y7I5lZKSgpSUFJ19aRpzWFiq9MojIiIiIiKi3MeeeCPZunUr1Go1rK2tUatWLdSrVw9z58596+2EEFCUd5/JMSdlXxUaGgpHR0ed7cDvU/XKIiIiIiIiepWAki+3goiNeCMJDAxEVFQULl68iOTkZGzcuBHFihWDj48Prl69itTU1Ey3uXPnDhISElC2bFkAgI+PD86fP59lfkxMDABoy+ZUSEgI4uPjdbZ6bUbplUVERERERER5g414I7Gzs4O3tzc8PDxgaWmp3d+lSxc8e/YMixYtynSb6dOnw9LSEh06dNCWvXz5MrZs2ZKp7IwZM1CkSBE0atRIr/qpVCo4ODjobBxKT0REREREZFp4TbxktWrVwpAhQzBixAikpqaibdu20Gg0WLlyJWbPno1Zs2bB3d0dwItG/Pr16/H555/jxx9/xMcff4yEhATMnz8fmzdvxvr163Vmpk9PT0dUVJTO/VlZWcHPzy83HyIREREREb3nMjg7fa5hIz4XzJo1C5UqVcLPP/+M7777DoqioGrVqoiIiNCZiV5RFKxbtw6zZ8/GzJkzMWDAAKhUKtSqVQv79u1D3bp1dXKfPXuGKlWq6Ozz8PDAjRs3cuNhERERERERUS5jI94IwsPD31qmZ8+e6Nmz51vLWVhYYNiwYRg2bNgbywUHByM4OPgda0hEREREREQFARvxREREREREZBAhCuZM8PkRJ7YjIiIiIiIiMhFsxBMRERERERGZCA6nJyIiIiIiIoMIzk6fa9gTT0RERERERGQi2IgnIiIiIiIiMhEcTv8ey0iXN+blabKcl5ZVxcpScgEg1cJKWnbVuaOl5B64K+8tHJdiIyXXwdlRSi4APElRS8uW5bZ5aSm5qT5y/v8AIAFOUnKfquS9Nko4JUvLtgloKCVXXJH4GZ0k5xy+ytNTSi4APC1ZQUpuwP5QKbkAEFk/REpuvT9/kpILAIqkyaWfql3kBAMoVtRSWjaQJiXV2jxVSi4AOKQ9lpIrJPb9PbRyk5Jr5ZAgJRcALDTPpWWbqgxwdvrcwp54IiIiIiIiIhPBRjwRERERERGRieBweiIiIiIiIjIIZ6fPPeyJJyIiIiIiIjIRbMQTERERERERmQg24vNIbGwsBg0aBC8vL6hUKri7u6NVq1bYs2cPAMDT0xOKokBRFNja2qJChQpYtGhRppxy5crBysoK//77b24/BCIiIiIiIgCAEEq+3PSxYMEClC5dGtbW1qhWrRoOHjyYbdmNGzeiUaNGKFq0KBwcHFCrVi3s2LFD36fxnbARnwdu3LiBatWqYe/evZg2bRrOnTuH7du3IzAwEAMGDNCWmzhxIu7evYvo6Gi0bdsW/fr1w9q1a7XHDx06hOTkZHTs2BHh4eF58EiIiIiIiIgKjrVr1+Krr77CN998gzNnzuCjjz5Cs2bNcPPmzSzLHzhwAI0aNcK2bdtw6tQpBAYGolWrVjhz5oy0OrIRnwf69+8PRVFw/PhxfPLJJ/Dx8YG/vz+GDh2Ko0ePasvZ29vDxcUF3t7emDRpEsqWLYuIiAjt8aVLlyIoKAjdu3dHWFgYBGeTICIiIiIi0ttPP/2EXr16oXfv3ihfvjxmzZoFd3d3/Pzzz1mWnzVrFkaOHIkPP/wQZcuWxZQpU1C2bFls2bJFWh05O30ue/z4MbZv347JkyfDzs4u03EnJ6dsb2ttbQ2NRgMAePr0KdavX49jx47B19cXiYmJiIyMRGBgoKyqExERERERZSkjn/YnpqSkICUlRWefSqWCSqXKVDY1NRWnTp3C6NGjdfY3btwYhw8ffqf7y8jIwNOnT1G4cGH9K/0W7InPZVeuXIEQAr6+vu98m7S0NISHh+PcuXP4+OOPAQBr1qxB2bJl4e/vD3Nzc3Tp0gVLly7NNiMlJQUJCQk6W5omJdvyREREREREpi40NBSOjo46W2hoaJZlHz58iPT0dBQvXlxnf/HixREbG/tO9zdjxgwkJiaiU6dOBtc9O2zE57KXQ94V5e2TLIwaNQpqtRo2NjYYMGAARowYgb59+wJ4MZS+W7du2rLdunXDxo0bERcXl2VWVi/eg1umGv6AiIiIiIiI8qmQkBDEx8frbCEhIW+8zettNSHEO7XfVq9ejfHjx2Pt2rUoVqyYQfV+Ezbic1nZsmWhKApiYmLeWnbEiBGIiorCP//8g2fPnmHatGkwMzPD+fPncezYMYwcORIWFhawsLBAzZo18fz5c6xevTrLrKxevB+1GmXsh0dERERERO8hIfLnplKp4ODgoLNlNZQeAJydnWFubp6p1/3+/fuZeudft3btWvTq1Qvr1q1Dw4YNjfa8ZoWN+FxWuHBhNGnSBPPnz0diYmKm46/2pDs7O8Pb2xtubm46Z36WLl2KevXq4ezZs4iKitJuI0eOzHZIfVYvXgvLrF+8RERERERE7xsrKytUq1YNu3bt0tm/a9cu1K5dO9vbrV69GsHBwVi1ahVatGghu5psxOeFBQsWID09HdWrV8eGDRtw+fJlxMTEYM6cOahVq9Ybb6vRaPDrr7/i008/RYUKFXS23r1749SpUzh79mwuPRIiIiIiIqKCY+jQoViyZAnCwsIQExODr7/+Gjdv3kS/fv0AvBjh/Nlnn2nLr169Gp999hlmzJiBmjVrIjY2FrGxsYiPj5dWRzbi80Dp0qVx+vRpBAYGYtiwYahQoQIaNWqEPXv2ZLt0wUubN2/Go0eP0K5du0zHypYti4oVK75xgjsiIiIiIiJjE1Dy5ZZTnTt3xqxZszBx4kRUrlwZBw4cwLZt2+Dh4QEAuHv3rs6a8YsWLUJaWhoGDBgAV1dX7TZkyBCjPbev4xJzecTV1RXz5s3DvHnzsjx+48aNLPd36NAB6enp2eZGR0cbo3pERERERETvpf79+6N///5ZHgsPD9f5OzIyUn6FXsOeeCIiIiIiIiITwZ54IiIiIiIiMkiGyOsavD/YE09ERERERERkItiIJyIiIiIiIjIRHE5PREREREREBhEcTp9r2BNPREREREREZCLYE/8eS0+Xd7rMwlxSdkaGnFwAlnGx0rIVSacmNRp5z4fKIk1KbnJispRcALC1SJWUbC0pFyhk/kRKbpHYGCm5AJBRvIKUXDOR/fKZhrL55y9p2bJYWMg7z26jkvQZXbionFwA6gfXpOQqifFScgGg3p8/Sck9UGeolFwAMDsu573i9OS6lFwASE72lZZtY66RkpuUJu97Jc3SUkquRbqs71jA5bmc97f1nUtScgEg0aOStGyit2EjnoiIiIiIiAzC4fS5h8PpiYiIiIiIiEwEG/FEREREREREJoLD6YmIiIiIiMggGULJ6yq8N9gTT0RERERERGQi2IjPp4KDg6EoSqbtypUrOHPmDFq2bIlixYrB2toanp6e6Ny5Mx4+fJjX1SYiIiIiIiKJOJw+H2vatCmWLVums09RFNSoUQOtWrXCjh074OTkhOvXr2Pz5s1ISkrKo5oSEREREdH7jLPT5x424vMxlUoFFxcXnX0RERFISEjAkiVLYGHx4r+vdOnSaNCgQV5UkYiIiIiIiHIRh9ObGBcXF6SlpWHTpk0QPN1FRERERET0XmEjPh/bunUr1Gq1duvYsSNq1qyJMWPGICgoCM7OzmjWrBl+/PFH3Lt3L6+rS0RERERE7ykh8udWELERn48FBgYiKipKu82ZMwcAMHnyZMTGxmLhwoXw8/PDwoUL4evri3PnzmWblZKSgoSEBJ0tTZOSWw+FiIiIiIiIjICN+HzMzs4O3t7e2s3V1VV7rEiRIujYsSNmzJiBmJgYuLm5Yfr06dlmhYaGwtHRUWf7c+u03HgYREREREREZCRsxBcAVlZWKFOmDBITE7MtExISgvj4eJ2tTsuRuVhLIiIiIiIqqDJE/twKIs5Ob2K2bt2KNWvWoEuXLvDx8YEQAlu2bMG2bdsyLUf3KpVKBZVKpbPPwjJVdnWJiIiIiIjIiNiINzF+fn6wtbXFsGHDcOvWLahUKpQtWxZLlixB9+7d87p6REREREREJBEb8flUeHh4lvu9vLzwyy+/5G5liIiIiIiI3kAIJa+r8N7gNfFEREREREREJoKNeCIiIiIiIiITweH0REREREREZBBRQGeCz4/YE09ERERERERkItiIJyIiIiIiIjIRHE5PREREREREBsngcPpcw0b8eyw9Xd477dItcym5SqluUnIB4HmqvIEpalW6lNykq2lScgHgn4e2UnKLuTtLyQWASw+cJCUnS8oFDt0uIyW3kNpDSi4APLot56ujsFrO+wQAkov6Ssu2tpTzWZr+WN7zobLIkJJ7zOUTKbkAEP9cJSXXwkHOcwEAiqTVlsyO/yUnGEBG9QpScrfsuyAlFwDM5PzkAACkZsj5vPv7tp2UXABIKi7ne8VMkfe7MUPS0mQJzrWl5AJAEZEiJTdQSioVNBxOT0RERERERGQi2BNPREREREREBuHs9LmHPfFEREREREREJoKNeCIiIiIiIiITweH0REREREREZBAOp8897IknIiIiIiIiMhEFvhF///599O3bF6VKlYJKpYKLiwuaNGmCI0eOAAA8PT2hKEqm7YcffgAA3LhxQ2e/o6MjatasiS1btgAATp06BUVRcOjQoSzvv0mTJmjdurX279u3b8PKygq+vlkvd6QoCqytrfHPP//o7G/bti2Cg4O1Zd60vSxHREREREREBUuBH07foUMHaDQaLF++HF5eXrh37x727NmDx48fa8tMnDgRffr00bmdvb29zt+7d++Gv78/4uLisGDBAnTo0AGnT59GtWrV8J///AfLli1D3bp1dW5z69Yt7N69Gxs3btTuCw8PR6dOnXDgwAH8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Y8eO6NmzJypVqgR7e3ucPHkS06ZNQ5s2bbTlnj59mqnxbWtrCwcHB9SoUQMjR47EsGHD8O+//6Jdu3Zwc3PDlStXsHDhQtStWxdDhgxB48aNUb58eXTp0gWTJ0+Gm5sboqOjMXz4cPTr109nybqsDBs2DB07dsTIkSNRokQJKc8HERERERFRbskooEPX86MC0xOvVqtRo0YNzJw5E/Xq1UOFChXw3XffoU+fPpg3b5623NixY+Hq6qqzjRw5Unt86tSpWLVqFY4dO4YmTZrA398fQ4cORaVKlfD5558DeDGEfefOnfDy8kLXrl3h7++P0aNHo3fv3vjpp5/eWteWLVvC09Mz13vjiYiIiIiIyLQVmJ54lUqF0NDQNy6zduPGjXfK6tSp01tnj3dxcUFYWNgby3h6ekJkMZuCoii4cOGC9u/g4GDtNfvvcvtXvTppHxERERERERVsBaYRT0RERERERHmjoM4Enx8VmOH0RERERERERAUdG/FEREREREREJoLD6YmIiIiIiMggIt9OT6/kdQWMjj3xRERERERERCaCjXgiIiIiIiIiE6GIt61hRgXWyIXPpWVnmODLKv6JvOejuJu9lFyVSt55uMePkqXkqlTyruLRaNKl5Mqss4WFnCFeFhbyXhsPHiRJybWxtpSSCwBPHsupMwAUdraVktu8jrzP0b2n5DzXaWkZUnIBwNzc9IZDFisq53lOTpb32jCT9DxfuhAnJRcAWn1bU1r232tipOQOKrJWSi4AzLr/5mWS9WVjLe97JVUj5zV99668z/5ixWyk5IZ0MpeSmxumbZD3HWCIkR0KXr91wXtERERERERERAUUG/FEREREREREJoKz0xMREREREZFBTPBqWpPFnngiIiIiIiIiE8FGPBEREREREZGJYCM+H7p//z769u2LUqVKQaVSwcXFBU2aNMGRI0e0Zc6cOYOOHTuiePHisLa2ho+PD/r06YNLly7lYc2JiIiIiOh9lJEh8uVWELERnw916NABZ8+exfLly3Hp0iVs3rwZAQEBePz4MQBg69atqFmzJlJSUvDbb78hJiYGv/76KxwdHfHdd9/lce2JiIiIiIhIFk5sl8/ExcXh0KFDiIyMRP369QEAHh4eqF69OgAgKSkJPXr0QPPmzbFp0ybt7UqXLo0aNWogLi4uL6pNREREREREuYA98fmMWq2G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iIiITAR74omIiIiIiMggHE2fe9gTT0RERERERGQi2IgnIiIiIiIiMhEcTk9EREREREQG4ez0uYc98ZIEBwdDURQoigILCwuUKlUKX375JZ48eYILFy5AURQcO3ZM5zY1atSASqVCUlKSdl9qaipsbW3xyy+/aHPbtm2b6f4iIyOhKAri4uJkPiwiIiIiIiLKQ2zES9S0aVPcvXsXN27cwJIlS7Blyxb0798fvr6+cHV1xb59+7Rlnz17hjNnzqBYsWI4fPiwdv+xY8fw/PlzBAYG5sVDICIiIiIionyEjXiJVCoVXFxcULJkSTRu3BidO3fGzp07AQABAQGIjIzUlj148CB8fHzQunVrnf2RkZEoUaIEypaVs34mERERERGRoYQQ+XIriNiIzyXXrl3D9u3bYWlpCQAIDAzEoUOHkJaWBgDYt28fAgICUL9+fZ0e+n379rEXnoiIiIiIiACwES/V1q1boVarYWNjgzJlyuD8+fMYNWoUgBc98YmJiThx4gSAFz3u9evXR/369XHy5EkkJSUhNTUVR48ezdSIf5n76tasWbNcf3xERERERESUuzg7vUSBgYH4+eefkZSUhCVLluDSpUsYNGgQAKBs2bIoWbIkIiMj4e/vjzNnzqB+/fooVqwYSpcujT///BMqlQrPnz9HgwYNssx91bFjx9CtW7ds65KSkoKUlBSdfWkaBRaWKiM9WiIiIiIiel9lcHb6XMOeeIns7Ozg7e2NSpUqYc6cOUhJScGECRO0xwMCArBv3z4cPHgQZcuWRbFixQBAO6R+37598PDwgKenZ5a5r24lSpR4Y11CQ0Ph6Oios/25dZrRHzMRERERERHJw0Z8Lho3bhymT5+OO3fuAHjRo3748GHs2rULAQEB2nL169dHZGQkIiMjM/XC6yskJATx8fE6W52WI42STURERERERLmDjfhcFBAQAH9/f0yZMgXAi0Z8YmIiwsLCUL9+fW25l9fFZ3U9vL5UKhUcHBx0Ng6lJyIiIiIiY8jrWeg5Oz1JM3ToUCxevBi3bt1C6dKl4eHhgadPn+o04kuUKIFSpUohOTmZM9MTERERERGRFie2kyQ8PDzL/UFBQQgKCtL+fePGjSzLXblyJUe5AQEBBfZMExEREREREb3ARjwREREREREZRHB2+lzD4fREREREREREJoKNeCIiIiIiIiITweH0REREREREZBAOp8897IknIiIiIiIiMhFsxBMRERERERGZCA6nf4+ZmyvSsi0t5AynsdE8lZILAAmWRaRlF06+IyVXk+oiJRcANOmm9/GQkmZ65yXVVilSch3ME6TkAsCtFDmvOyvzdCm5AJAKlbRsh7THUnLt1G5ScgHAwlxOrnWSnOcCAFSW9lJyZX6vCEl9JRbpqVJyAcBMkfP9rcmQ951iYy3vs1+TYSkl11zi11XdY/Ol5B6qMUBKLgD4x2yRkpuuyHvdmUt8H5qqDC53nWtM7xcvERERERER0XuKjXgiIiIiIiIiE2F642WJiIiIiIgoX+Hs9LmHPfFEREREREREJoKNeCIiIiIiIiITweH0REREREREZBDB2elzDXvi88j9+/fRt29flCpVCiqVCi4uLmjSpAlCQ0OhKMobt/DwcERGRursK1q0KJo1a4azZ8/m9UMjIiIiIiIiSdgTn0c6dOgAjUaD5cuXw8vLC/fu3cOePXvg5+eHu3fvassNGTIECQkJWLZsmXafo6Mjjh07BgC4ePEiHBwccPPmTQwePBhNmzbFhQsX4OjomOuPiYiIiIiIiORiIz4PxMXF4dChQ4iMjET9+vUBAB4eHqhevXqmsjY2NkhJSYGLi0uWWcWKFYOTkxNcXFwwY8YM1K1bF0ePHkWTJk2kPgYiIiIiIqKXMjg7fa7hcPo8oFaroVarERERgZSUFKPl2tjYAAA0Go3RMomIiIiIiCj/YCM+D1hYWCA8PBzLly+Hk5MT6tSpgzFjxiA6OlrvzEePHmHChAmwt7fPskc/JSUFCQkJOluaxngnEIiIiIiIiEg+NuLzSIcOHXDnzh1s3rwZTZo0QWRkJKpWrYrw8PAc5ZQsWRJqtRrOzs6IiYnB+vXrUaxYsUzlQkND4ejoqLMd3DLVSI+GiIiIiIjeZyJD5MutIGIjPg9ZW1ujUaNGGDt2LA4fPozg4GCMGzcuRxkHDx7E2bNnER8fj0uXLmV7LXxISAji4+N1to9ajTLGwyAiIiIiIqJcwont8hE/Pz9ERETk6DalS5eGk5PTW8upVCqoVCqdfRaWvHaeiIiIiIjIlLARnwcePXqEjh07omfPnqhUqRLs7e1x8uRJTJs2DW3atMnr6hEREREREeWIEAVz6Hp+xEZ8HlCr1ahRowZmzpyJq1evQqPRwN3dHX369MGYMWPyunpERERERESUT7ERnwdUKhVCQ0MRGhr61rLZTXQXEBDAs11ERERERETvGTbiiYiIiIiIyCAiIyOvq/De4Oz0RERERERERCaCjXgiIiIiIiIiE8Hh9ERERERERGSQjAzO15Vb2BNPREREREREZCLYiCciIiIiIiIyERxO/x5LTZU5g6S5lFShyDvvZJvxVFp2spW9tGxZrCxMb0iUtSVnRc0NhayfSclNy5D3leT8/Ja0bAVy3itm5oqUXACwtpLzXolzLCUlFwDsUp5IyU03s5KSCwAPrdyk5Lo8vyYlFwAyhJzXXVHlnpRcAEjVFJKW/SxVJSXXwkzed+x9x7JScv1jtkjJBYC/y7eSklvr1BIpuQCQYFtcSq6zlNTcweWvcw974omIiIiIiIhMBBvxRERERERERCaCw+mJiIiIiIjIIIKz0+ca9sQTERERERERmQg24omIiIiIiIhMBBvx+UxwcDDatm2baX9kZCQURUFcXJzOv1+6c+cOKlSogLp16+rsJyIiIiIikk1kiHy5FURsxBcAV69eRd26dVGqVCns3LkTTk5OeV0lIiIiIiIikoCNeBMXHR2NunXrokaNGvj9999ha2ub11UiIiIiIiIiSTg7vQk7fPgwunbtiqCgIMydOxdmZjwnQ0REREREuS9DZOR1Fd4bbMTnQ1u3boVardbZl56enqlcu3bt0LlzZ8yfP/+tmSkpKUhJSdHZl6YBLCxVhlWWiIiIiIiIcg27bvOhwMBAREVF6WxLlizJVK5NmzbYtGkTDh48+NbM0NBQODo66myHt02TUX0iIiIiIiKShI34fMjOzg7e3t46W4kSJTKVW7RoET799FM0a9YM+/fvf2NmSEgI4uPjdbbazUfKeghEREREREQkAYfTmzBFUbBo0SKYm5ujefPm+OOPPxAQEJBlWZVKBZVKd+i8hWVKlmWJiIiIiIhyoqAu55YfsRFv4hRFwYIFC2Bubo4WLVpgy5YtaNCgQV5Xi4iIiIiIiCRgI74AUBQF8+bNg7m5OVq2bInNmzejYcOGeV0tIiIiIiIiMjI24vOZ8PDwLPcHBARACJHp36+aPXs2Zs+eLbN6REREREREmXA4fe7hxHZEREREREREJoKNeCIiIiIiIiITweH0REREREREZJCsLvclOdgTT0RERERERGQi2IgnIiIiIiIiMhEcTk9ERERE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tGzZUmdSO19fX2zatAkAkJaWhk8++QQnT57Eb7/9hvT0dMTGxiI2NhapqanvfN9sxOczLVu2RLFixRAeHq6zPykpCWvXrkWvXr20+4oUKQIXFxdUqlQJixYtQlJSEnbu3JnLNSYiIiIiovedyMjIl5tMv/32GypWrIjGjRujcePGqFSpEn799VedMhcvXkR8fDwA4Pbt29i8eTNu376NypUrw9XVVbsdPnz4ne+Xw+nzGQsLC3z22WcIDw/H2LFjtZMirF+/Hqmpqejatav2RfAqW1tbAC+GZxAREREREZFchQsXxsqVK99YRoj/myvA09NT5299sSc+H+rZsydu3LiByMhI7b6wsDC0b98ehQoVylQ+MTERISEhMDc3z/aa+JSUFCQkJOhsaZqULMsSERERERFR/sRGfD7k6+uL2rVrIywsDABw9epVHDx4ED179tQpV7t2bajVatjb22PLli0IDw9HxYoVs8zMan3EQ1unSn8sRERERERU8IkMkS+3goiN+HyqV69e2LBhAxISErBs2TJ4eHjg448/1imzdu1anD17Fg8ePMC///6Lbt26ZZuX1fqIdVuOkv0wiIiIiIiIyIjYiM+nOnXqBHNzc6xatQrLly9Hjx49tNfHv+Tu7o4yZcq807IEKpUKDg4OOpuF5buvl0hERERERER5jxPb5VNqtRqdO3fGmDFjEB8fj+Dg4LyuEhERERERUZaEkDsTPP0f9sTnY7169cKTJ0/QsGFDlCpVKq+rQ0RERERERHmMPfH5WK1atbJcgsBYSxMQERERERGRaWEjnoiIiIiIiAxSUGeCz484nJ6IiIiIiIjIRLART0RERERERGQiOJyeiIiIiIiIDCIyODt9bmFPPBEREREREZGJYCOeiIiIiIiIyFQIoneQnJwsxo0bJ5KTk00iV2Y265w72aZYZ5nZrHPuZLPOuZNtinWWmc06504265w72aZYZ5nZMutM7y9FCC44Tm+XkJAAR0dHxMfHw8HBId/nysxmnXMn2xTrLDObdc6dbNY5d7JNsc4ys1nn3MlmnXMn2xTrLDNbZp3p/cXh9EREREREREQmgo14IiIiIiIiIhPBRjwRERERERGRiWAjnt6JSqXCuHHjoFKpTCJXZjbrnDvZplhnmdmsc+5ks865k22KdZaZzTrnTjbrnDvZplhnmdky60zvL05sR0RERERERGQi2BNPREREREREZCLYiCciIiIiIiIyEWzEExEREREREZkINuKJiIiIiIiITAQb8URERESUJ549e5bXVSAiMjlsxBMR5TMajQY9evTAtWvXTCrbFN28eROmtkjLgQMHkJaWZtTM9PR0REdH4/nz55mOJSUlITo6GhkZGUa9T8rauXPn8NVXX+V1NXT07NkTT58+lZJdsWJFHDhwQEq2TOvXr0fXrl3RqVMn/PLLL7l638Z+/xvq6dOn2LVrF7Zt24aHDx/mdXXy1D///IPFixdjwYIF+Pvvv/O6OlSAcYk5KlD+/fdf/Pnnn7h//36mH5yDBw82KLtnz56YPXs27O3tdfYnJiZi0KBBCAsLe+eszZs3v3PZ1q1bv3PZ7KSmpuL69esoU6YMLCwsDM7LLcnJybC2ts7ramSSG/9/Tk5OOH36NLy8vPS6fV5lZyUuLg5OTk4G53h5eeHEiRMoUqRIpvyqVavqdWLC3Nwcd+/eRbFixQyu3+u57yI9PV2vbGPXOTw8HPPmzcOxY8cy1T09PR01atTAV199hW7duul9H48ePdL+3926dQuLFy/G8+fP0bp1a3z00UcG1T8vxMTEoEWLFkY5IZaQkIDVq1dj6dKlOHnyJCpVqoSoqCjDK2kkst4nADBy5EjMmjULgwYNwpQpU4y2lvbly5cxduxYLFq0CA4ODjrH4uPj8eWXX2LSpEl6fQ7+8ssv6NevH8qWLQtra2v89ddfGDlyJEJDQw2u95o1a9ClS5dsj2s0GnzyySf4/fffc5SbkJDwTuVef67eJjo6Gs2aNUNsbCyEEHBwcMB///tfNGzYMEc5WUlISHhrffbu3YsGDRoYfF8vpaamIjU1FWq1Ose3PXDgAJo3b46kpCQAgIWFBZYvX45PP/3UaPUj0hJEb3DgwAHRtWtXUbNmTXH79m0hhBArVqwQBw8ezHe5YWFhwsrKSqjVauHh4SE8PT21W+nSpQ2qrxBCmJmZiXv37mXa/+DBA2Fubp6jLEVR3mkzMzMzqM6JiYmiZ8+ewtzcXJibm4urV68KIYQYNGiQCA0NNSh7xYoVonbt2sLV1VXcuHFDCCHEzJkzRUREhEG56enpYuLEicLNzU2nzt9++61YsmSJQdnHjh0TU6dOFcOGDRNff/21zpYTWf0/vf73y01fwcHBYsaMGXrfPq+yf/jhB7FmzRrt3x07dhRmZmbCzc1NREVFGZStKEqW78HY2FhhZWVl1ExDKYoiPD09xbhx40RERES2m77Zxq5z3bp1xerVq7M9vnbtWvHRRx/plR0dHS08PDyEmZmZKFeunDhz5owoXry4UKvVwsHBQZibm4tNmzbplf3qe+1NmwxRUVEGZ0dGRoru3bsLW1tbYWZmJkaNGiUuX76sd96jR4/ErVu3dPb99ddfIjg4WHTs2FH89ttveuXKep+8dOTIEVG+fHnh5+cnTp06ZZTMPn36iBEjRmR7fOTIkaJfv356ZVeoUEF8++232r+XLVsm1Gq1XlmvU6lUYvv27VkeS0tLE23atBFubm45zn39u+n1Td/fHM2aNRM1a9YUf/75pzh16pRo3bq1KFeuXI5zsvLRRx+J58+fZ3t87969ws7OTu/8sLAwMXDgQLFy5UohhBCjR48WVlZWwszMTDRs2FA8fPgwR3n16tUTLVu2FP/++694/Pix6Nu3ryhZsqTe9SN6EzbiKVv//e9/hY2Njejdu7dQqVTaxtT8+fNFs2bN8l1uyZIlxaRJk0R6erreGVmJj48XcXFxQlEUceXKFREfH6/dHj9+LJYvXy5cXV2Nep/GMnjwYFGtWjVx8OBBYWdnp32uf//9d1G5cmW9cxcsWCCcnZ3FpEmThI2NjTZ32bJlIiAgwKA6T5gwQXh5eYmVK1fqZK9du1bUrFlT79zJkycLRVGEr6+vqF+/vggICNBugYGBeufu2rVLVK1aVWzfvl3Ex8eLhIQEsX37dvHBBx+InTt36p07adIk4eTkJDp06CCmTJkiZs+erbMZQmZ26dKlxZ9//imEEGLnzp3CyclJ7NixQ/Tq1Us0atRIr8zff/9d/P7770JRFLFixQrt37///rvYuHGjGDBggPDx8dErW1bj5Pjx46Jfv37CyclJVKlSRcydO1c8fvzYKNmKooj79+8bJeulokWLiuvXr2d7/Nq1a8LZ2Vmv7KZNm4qWLVuKgwcPir59+4oSJUqIHj16iPT0dJGeni769+8vatSooVe2zJMlb6NvI/7OnTti8uTJokyZMsLFxUV8/fXX4sSJE8LCwkL8/fffBtWpS5cuOicl7927JwoVKiT8/f1F69athaWlpVixYkWOc2W85l6XnJwshg8fLqytrUWrVq1Eu3btdLacKleunDh+/Hi2x0+ePKn354atra32u0mIF41rS0tLcffuXb3yXjVr1ixhZ2cnDh8+rLM/LS1NtG3bVhQvXlzExMTkODcyMlK77du3T9jY2IjffvtNZ39kZGSOc4sWLSpOnDih/fvhw4fCzMxMPH36NMdZr/P39xctW7YUaWlpmY5FRkYKOzs7MWTIEL2yX/5++fjjj0XhwoVFv379hIuLi/jhhx/EtGnTRMmSJXN8kqdQoULi3Llz2r+fPXsmzMzMjPbZT/QqNuIpW5UrVxbLly8XQgihVqu1X1gve1HyW27hwoXFlStX9L59dt529trc3FxMmjTJ6PdrDKVKlRJHjhwRQug+15cvXxb29vZ655YvX17bc/Zq7rlz50SRIkUMqnOZMmXE7t27M2XHxMQIJycnvXOLFSsmli1bZlDdsuLv75/lCJIDBw4IX19fvXNfHUny+mboyBKZ2dbW1uLmzZtCiBcnkb744gshhBAXL17U+/8vuxEPiqIIKysr4ePjI7Zs2aJ39uTJkzOdyDDWiY3nz5+LX3/9VTRo0EDY2tqKzp07G3Ry52Wd+/btm2k0iSGjS2xtbcXZs2ezPX727Flha2urV32LFCmizX769KlQFEXnR39MTIxwdHTUK1vmyZK30bcRr1KpRLdu3cT27dt1TjoboxHv6ekp9u3bp/37xx9/FGXKlBEajUb7tz4nTBRFEU5OTqJQoUJv3AwRHx8vPvvsM2FjYyO6desmgoODdbacsra21o4Sy8qNGzeEjY2NXnXN6uTfq99Xhho7dqxOgzAtLU20b99eFCtWzODXyEvGqm92z8W1a9cMzv7333+Fl5eX6Nq1q87+/fv3C7VaLQYOHKh3tre3t1i1apUQQogTJ04IMzMzsX79eu3xbdu2iVKlSuUoU+ZzQfQ607k4lnLdxYsXUa9evUz7HRwcEBcXl+9ye/XqhfXr12P06NF6Z2Rl3759EEKgQYMG2LBhAwoXLqw9ZmVlBQ8PD7i5uRl0H/v378f06dMRExMDRVFQvnx5jBgxwuDrRB88eJDlNYyJiYlQFEXv3OvXr6NKlSqZ9qtUKiQmJuqdC7yY18Db2zvT/oyMDGg0Gr1zzczMUKdOHUOqlqWrV6/C0dEx035HR0fcuHFD79zr168bUKu8yy5UqBBu3boFd3d3bN++HZMmTQIACCH0uv4bgHZ+i9KlS+PEiRNwdnY2Wn0BYOHChW+8hl1RFL3n1LC2tka3bt3QrVs3XL9+Hb169ULTpk3x4MEDnc+SnDp37hysrKyyPZ7T93fZsmVx+PBhVKpUKcvjhw4dQtmyZXOU+dLjx4/h4uICAFCr1bCzs9N57IUKFdJ70rQPP/wQH374IWbOnIn//ve/WLZsGUaNGoVWrVqhV69eaNSokV65Mnl4eODQoUMoVaoUPDw84Ovra7Ts2NhYlC5dWvv33r170a5dO+1cKK1bt9b7uu0JEyZk+VlnDDt37kSvXr3g5uaG06dPG+U5cXR0xNWrV+Hh4ZHl8StXruT4+u9XLVmyROe66bS0NISHh+t8Pun7uTFhwgQ8fvwYjRs3RmRkJL755hscOHAAe/fuhZ+fn951lkFRFDx9+lQ7f40QQrvv1evw9Xmu3dzcsHPnTnz00UcYPHgw5syZg0OHDqFFixbo3r075s6dq3e9b968ibp16wIAPvjgA1hYWKBixYra45UqVcLdu3dznHv+/HnExsZq/xZCICYmRuczLrvPWaKcYCOesuXq6oorV67A09NTZ/+hQ4cMmhBLVm5oaChatmyJ7du3o2LFirC0tNQ5/tNPP+U4s3Dhwrh06RKcnZ3x+eefo2HDhpkmtjPUypUr0aNHD7Rv3x6DBw+GEAKHDx/Gxx9/jPDwcAQFBemd/eGHH+KPP/7AoEGDAPzfD/vFixejVq1aeueWLl0aUVFRmX4c/e9//zP4B4a/vz8OHjyYKXv9+vVZnjh4V19//TXmz5+PWbNmGVS/13344Yf46quvsHLlSri6ugJ48UN62LBhqF69ulHuQ/z/+UcNOfGSW9nt27dHUFAQypYti0ePHqFZs2YAgKioqCxPzuSErJMPJ0+elDJh10u3b99GeHg4wsPD8fz5c4wYMcKgxgMAbNq0yah1DgoKwrfffovatWtn+oF59uxZjB07FiNHjtQ7//XXl7FfyzJOlhQqVOiN9dR3hvCLFy/izz//xNKlS/Hhhx/Cx8dHO2Ggoc/Ly5PhLz8/jx8/jl69emmPK4qClJQUvbK7dOki5X3St29fLF++HGPGjME333zzzpNCvk29evUwd+7cbCc9mzNnjt4nykuVKoXFixfr7HNxccGvv/6q/duQk38AMHfuXMTFxeE///kP1Go19uzZo9PIzC+EEPDx8cm07+X39ctGvb4nccuUKYPt27cjICAACQkJ2LRpE4KCgrBgwQKD6q3RaHQmUbSystL53WhhYaFXnbN6vbVs2RKKohj8XBC9io14ylbfvn0xZMgQhIWFQVEU3LlzB0eOHMHw4cMxduzYfJc7ZcoU7NixA+XKlQOg+2NI3x9GqampSEhIgLOzM1asWIFp06YZvRE/efJkTJs2DV9//bV235AhQ/DTTz/h+++/N6gRHxoaiqZNm+L8+fNIS0vD7Nmz8ffff+PIkSPYv3+/3rkjRozAgAEDkJycDCEEjh8/jtWrVyM0NBRLlizROxcAxo0bh+7du+Pff/9FRkYGNm7ciIsXL2LFihXYunWr3rnDhw9HixYtUKZMGfj5+WU6ybNx40a9cpcuXYr27dvDw8MDpUqVAvDiDL+Pjw8iIiL0ri8ArFixAj/++CMuX74MAPDx8cGIESPQvXt3g3JlZs+cOROenp64desWpk2bpu2punv3Lvr3729wvffs2YM9e/ZkuQJFTlaIeEnGiRHgxWfHpk2bsHTpUhw8eBDNmjXDrFmz0Lx5c5iZGba6q4w6f/311/jf//6HatWqoWHDhvD19YWiKIiJicHu3btRu3Ztnc+onAoODtb+YE5OTka/fv1gZ2cHAHo3Kl9n7JMlxj7h96o6deqgTp06mD17NtasWYOwsDCkp6ejf//+CAoKQtu2bVG0aNEc51avXh1z5szB4sWLsXHjRjx9+lSnUXHp0iW4u7vnOFfW+wQA/vzzTxw+fBhVq1Y1am5ISAhq1aqFTz75BCNHjtT+Nrhw4QKmTZuGHTt24PDhw3plGzLK6m2GDh2q/beTkxOEEKhcuTLCw8N1yunTMfE6Y/y/7tu3z+CM7Lzsyff09MRvv/2Gdu3aoW3btpg2bZrBvfyAbq+5EAIXLlzAs2fPAECvpfJOnTpl0AgropzgEnP0Rt988w1mzpyJ5ORkAC+GSw8fPhzff/99vsstVKgQZs6cieDgYIPq9qpGjRrh3r17qFatGpYvX47OnTvDxsYmy7L6NCCAF4/977//ztRLeeXKFVSoUEH7HOnr3LlzmD59Ok6dOoWMjAxUrVoVo0aNMviM/uLFizFp0iTcunULAFCiRAmMHz9ep9dHXzt27MCUKVN06jx27Fg0btxY78wBAwZg6dKlCAwMRPHixTP9eFm2bJne2RkZGdi9ezcuXLgAIQT8/PzQsGFDg34g/fTTT/juu+8wcOBA1KlTB0II/Pnnn5g/fz4mTZpkUINKZrZMEyZMwMSJE/HBBx/A1dU10/O7adOmHGeamZkhNjbW6D2MRYoUgb29PT7//HN0794923x9fnzKqrNGo8HMmTOxatUqXL58WdvDFhQUhK+//hp///03KleunOPcHj16vFM5fd6DWZ0s6dmzp1FOluS2mJgYLF26FL/++iseP36s1+VDZ86cQaNGjfD06VOkpaUhJCREe0kLAHTv3h12dnZYuHBhjnJlveaAF98d0dHRmZaONIatW7eiZ8+eePTokXafEALOzs5YsmSJ3kuAJicnY/fu3WjZsiWAFycMXj0ZZWFhgYkTJ+q1RGpgYOBbyyiKgr179+Yot3379jp/b9myBQ0aNNCeTHsppye0V6xYgc6dOxttacBXmZmZ6XzOvz5yzJCe7Td9Pujba25mZoYqVaqgd+/eCAoKknb5CRHARjy9g6SkJJw/fx4ZGRnw8/PTa+3M3Mh1cXHBwYMH9b5uMyv37t3DzJkzcfXqVWzcuBFNmjTJ9otKnwYEAHh7e2PEiBHo27evzv5FixZh+vTp2p7S/Orhw4fIyMiQOhzZGOzt7bFmzRq0aNHCaJlpaWmwtrZGVFQUKlSoYLRc4MUlCxMmTMBnn32ms3/58uUYP368QUPLZWYDwK+//opFixbh2rVrOHLkCDw8PDBr1iyULl0abdq00TvX1dUV06ZNM8pIhJcmTJiAESNGwNbW1miZgO4PxKxO5hjy43P58uXo0qWLlB/Nr4uLi8OqVauwdOlSREVF5bthoDJPlrz0/Plz7Nq1C5cuXYKiKPDx8UHDhg2zPaH7LtavX4+IiAhoNBo0bNgQX3zxhfZYWloaNm/enKnR9S6uXbsGtVqNI0eOwMXFBTVq1NA5/scff8DPz0/nuvm8JnMNeuDF/9/27dtx5coVCCFQrlw5NG7c2KD/v0WLFmHr1q3YsmULgBffL/7+/trMCxcuYMSIETq96nlN1sk0mf9/kZGR73QyvH79+jnO/ueff96pXHZzKmTlyJEjCAsLw7p166DRaNC+fXv06tXrnU7MEOVY7syfRyTflClTxKBBg6Tle3p65njN0HexYMECYWVlJfr16ydWrFghfv31V9G3b1+hUqnEwoULc5z36hJ4b9v0NWHCBLFnz55M+589eyYmTJigd65MpUqV0mtZnrfx8vIyeP3zrKhUqizXi7506ZJQqVT5Nlvm8oMyVqBwd3fXeV/PnTvXoPfGS68v25Tdpo8vv/xSZ/mmFStW6Pz95MkTg5brFEKIPXv2iK5duwobGxvh6+srvvnmG3H69GmDMmV4daUCY659/dLvv/8uihYtmmlVhKJFi4rNmzfrlblo0SKhKIrw8fERlSpVEmZmZmL06NF61/FVZmZmOrNjd+rUScTGxhqc26NHj7duPXv21Ctb1jKPR48eFdu2bdPZFx4eLjw9PUXRokVFnz59RHJysl7ZH330kdi4caP279dnev/1118NWhL1bd60dF5uk/X/J8S7/57RR1JSkujfv79wc3MTRYsWFZ9++ql48OCBUeqdlJQkwsPDRf369YWZmZnw8vISkyZNErdu3TJKPpEQQrAnnnTk5Mx/ToZcycp9Vbt27bB3714UKVIE/v7+RrvmOTds2rQJM2bMQExMDABoZ6fXp9fy9eFnWREGTq5iZmYGS0tLhIaG6vQ03Lt3D25ubgb11mU3mZSiKLC2toa3tzeCg4PfuVfhpWXLlmH79u1YtmyZUXtdly1bhvXr12PlypVGvRauQoUKCAoKwpgxY3T2T5o0CWvXrsW5c+fyZbafnx+mTJmCtm3bwt7eHmfPnoWXlxf++usvBAQE6HWd4UujRo2CWq3Gd999p3fG614fJuzg4ICoqCiDJtkEXlyfXbJkSWNUMZPXe75er7O+78OX15SHhYUhMTERnTp1wsKFC3H27FmDJqwMDAzM8j3t6OiIcuXKYcCAAXpdpw3gnef20Ken7vDhwwgICEDr1q0xbNgwlC9fHsCL62hnzJiBrVu3IjIyMseThFasWBFt27bVXj4WHh6OQYMG6T1D/6tefz2/+h40RLt27bI9lp6ejt27dyMlJUXvYc179+596+dnTmf0btasGQICAjBq1CgALy4tq1atGj7//HOUL18eP/74I/r27Yvx48fnuM4uLi7Ys2cP/P39AQBFixbFiRMntBP2Xrp0CR9++CHi4+NznP3Ss2fPYG5urjNiICoqCt999x22bduW4+d6yZIlaNCggcGvhdeZmZnh3r17es3h8C7Z79ITr8/rbsSIEViwYAG6du0Ka2trrF69GgEBAVi/fr0+Vc3W1atXsWzZMqxYsQJ3795Fo0aNsG3bNqPeB72fOLEd6Xj1+h0hBDZt2gRHR0d88MEHAF5M2hEXF5fjYX6ycl/l5ORk0O2zMmfOHHzxxRewtrbGnDlz3ljWkFlo27Vr98YfSTkhc5KZV61YsQIDBw5EdHQ0fvnllzcud5UTY8eOxeTJk9GsWTNUr14dQgicOHEC27dvx4ABA3D9+nV8+eWXSEtLQ58+fd45d86cObh69SqKFy8OT0/PTCd5Tp8+rVd958yZgytXrsDNzQ0eHh6Zri/UN3fChAno3LkzDhw4gDp16kBRFBw6dAh79uzBunXr9MrMjWyZyw8mJyfjl19+we7du1GpUiWjrEDxOmOd165QoQLmzp1r1KH/L71eR2PUuXnz5jh06BBatmyJuXPnomnTpjA3N8/xtdNZye46+ri4OGzbtg3z5s3DoUOH9LreXp/G+buaNGkSevTogUWLFunsr127NmrXro2+ffvi+++/z/EP8mvXrumchOzevTu++OILxMbGapfiy2+yu1zs999/x5gxY6BSqQyamPbjjz/O8nVsyIzeUVFROvPsrFmzBtWrV9fOKu/u7o5x48bp1YiPj4/XLtsHvFjO9VUZGRl6T9h4+/ZtdO7cGUePHoW5uTkGDhyISZMmoV+/fli9ejXatGmDQ4cO5Th3yJAhSE5ORokSJRAYGIjAwEA0aNBAOyGrIV6duDI7+nSkvPp7RgiB5s2bY8mSJShRokSOs7Kqz9KlS9GlSxcAQLdu3VCnTh2kp6cbbYUE4MXs+qNHj4a7uzvGjBmDHTt2GC2b3m9sxJOOV6+FGjVqlLYn5uUH2svZc3N6faGs3Ozuw1hmzpypPUs7c+bMbMsZupQM8OJExst14v38/PReTk3mj9pXBQYG4ujRo2jVqhUCAgL0nhPgdYcOHdL+YHnVokWLsHPnTmzYsAGVKlXCnDlzctSIb9u2rVHql1u5HTp0wLFjxzBz5kxERERoJ8w7fvy4QUvtyc6WufxgdHS0tqH3119/6RyTOXu2PqZMmYIBAwYgIiICv/zyi5RJu4xp586dGDx4ML788kujzisC4I2fncCLSSfHjBljUO/Uv//+iw0bNuhct96+fXuDfuwfOXIEU6dOzfb4gAED9Pq8ff78uc4cMObm5lCpVEhKStKrnq9SFEX6cn7AixnlR40ahTNnzmDgwIEYPXo0ChUqpHfesWPHjN6T++TJExQvXlz79/79+9G0aVPt3x9++KF2YtacKlmyJP766y/tjPevi46O1nskzujRo/Hs2TPMnj0bGzZswOzZs7F//3785z//waVLl/SezyAuLg5Hjx7F/v37sW/fPu0KMx4eHmjQoIG2Ye/m5pbjbHt7e4PmGMjO6+8vc3Nz1KxZ0yijCW7duqWzxGD16tVhYWGBO3fu6D0y6HX79+9HWFgYNmzYAHNzc3Tq1Mkok/8SAeA18ZQ9Z2dnceHChUz7L1y4IAoXLpzvcseNGydu3Lih9+3zyr1790RgYKBQFEUUKlRIODk5CUVRRIMGDcT9+/cNzn/8+LH48ccfRc+ePUWvXr3E9OnTxaNHjwzKfPW6y/j4eNGkSRNRsmRJsXXrVoOuPxVCCDs7uyyv1758+bKws7MTQghx5coVYWtra9D9kBxhYWGiRIkSYs2aNcLOzk6sXr1aTJo0Sfvv/EZRFDF58mQxe/ZsMXv2bGFtbS2+++477d8vN31cu3ZNBAYGiuLFi4vff//dqHV+9RrU16/HjY2NzfH78PDhw6J3797CwcFBVK9eXcydO1fcv39fWFhYiL///ttodc/K2bNnhYuLi963nz9/vlCpVEJRFOHk5CQcHR2FoihCpVKJ+fPn651rbW39xu+UGzduCBsbmxznvv6ay+51pw9FUUTz5s1Fu3btRLt27YSFhYVo3Lix9u+Xm77++usv0bJlS2FhYSF69uxplGt8ZV1TXapUKbF//34hhBApKSnCxsZG7N69W3s8OjpaFCpUSK/swYMHCz8/P/H8+fNMx5KSkoSfn58YPHiwXtlubm7i0KFDQggh7t69KxRFEaGhoXplvUlqaqo4cOCAmDBhgggMDBS2trbC3Nw8xzkyr4l/3eufdYYwMzPL9BtLrVaLa9euGZR78+ZNMXHiROHl5SUURRF16tQRYWFh4tmzZwblEr2OPfGUrbS0NMTExGQ60xwTE5Npfeb8kLtlyxZMmjQJ9evXR69evdC+fXu9lnd51bvOLKsoCmbMmKHXfQwaNAgJCQn4+++/da65/PzzzzF48GCsXr1ar1zgxVng1q1b61y6MGfOHEycOBGbN2/Wu9devDLs0cHBAdu2bcNXX31llF7pwoULY8uWLZmWOduyZYv2msnExETY29vrlW+sEQ+5IT09HRERETr1bd26tVGG+snK7tGjB9LS0jBy5EgkJSUhKCgIJUqUwOzZs7XDFg115coVXL16FfXq1YONjY12uK0+SpUqpR1eC7y41vXXX3/VKaPvSJvSpUtj7969mDdvHjp06IDy5cvrDMEF9L/cYuzYsdq5HVJTUzF58mTtZUv69OjWqlULtWrV0lm3fOjQocjIyMCuXbvg7u6u93vubWxsbPReSvOPP/7A4MGD8dVXX2HYsGFwdXUFANy9exc//vgjhgwZAk9PTzRv3jzH2T4+Pti7d2+282/s2bMn09Kg7+L11xyQ+XWn72vu888/1/m7W7duOc7Iyq1btzB27FisXLkSLVu2RHR0tPb7Kr9q2rQpRo8ejalTpyIiIgK2trY6Pa/R0dEoU6aMXtljxozBunXrUK5cOQwcOBA+Pj5QFAUXLlzAvHnzkJaWlmnOkXcVGxurrZeLiwtsbGwMWtUjO+np6UhNTUVKSgpSUlKQlpamVy9/fhsF9a6EEJkuA0hOTka/fv10LovLyWUAjRo1wr59+1C0aFF89tln6NmzZ7ajNYgMxUY8ZatHjx7o2bMnrly5gpo1awIAjh49ih9++CHHk4rlRu6pU6cQHR2NZcuW4euvv8aAAQPQpUsX9OzZEx9++KFemWfOnHmncoZ8iW3fvh27d+/W+UHk5+eH+fPnG7QuOvBiuGfnzp3x888/Z7p0YcCAAZmGJL+rZcuW6cxzYGZmhjlz5qBKlSo4cOCAQXX+7rvv8OWXX2Lfvn2oXr06FEXB8ePHsW3bNu31ubt27crxCYj79++jS5cuiIyMhJOTE4QQiI+PR2BgINasWaP3UM709HTMnDkT69atw82bN5Gamqpz/PHjx3rlXrlyBS1atMDt27dRrlw5CCFw6dIluLu7448//tD7x6fsbADo06cP+vTpY/TlBx89eoROnTph3759UBQFly9fhpeXF3r37g0nJye9TqTduHHDKHXLzj///IMNGzagcOHCaNOmTaZGvD7q1auHixcvav+uXbs2rl27lqmMPmxtbdGzZ0/07NkTFy9exNKlS/HDDz9g9OjRaNSoETZv3mxQ3bOyc+dO+Pj46HXbadOmYfTo0TproQMvliP86aefYGtri6lTp+rViA8ODsbw4cNRvHjxTLf/448/MHLkSHzzzTc5zpX5mpNxWRkAlCtXDoqiYNiwYahduzYuX76c5fKn+qy7Xr9+faPNqfKqSZMmoX379qhfvz7UajWWL1+ucz9hYWF6f8cWL14chw8fxpdffonRo0frrF/eqFEjLFiwQGcof069ejLVzMzM4A4J4EUD9fDhw4iMjMTevXtx8uRJeHl5oV69ehg4cCDq16+v11B6kcvzYxvrpMHrJ7wAw0962djYYMOGDWjZsqVRr6snylLeDQKg/C49PV1MnTpVuLm5aZfVcXNzE1OnThVpaWn5LvdVGo1GbNy4UbRq1UpYWlqKChUqiFmzZom4uDij5BuTWq0WZ86cybT/9OnTwt7e3qBsa2vrbC9dsLa2NihbpkOHDokuXbqIKlWqiMqVK4suXbqIP//806DMTp06iWrVqonz589r9/3999/igw8+EF26dNE797vvvhOurq7ixx9/FNbW1uL7778XvXr1EkWKFNF7SKwQQjRr1kw0bdpU59KHhw8fiqZNm4rmzZvrnSs7W6bu3buLJk2aiFu3bukMq9yxY4fw8/PL49pl9ssvvwh7e3vRrl07o1wak1fS0tLEpk2bRKtWrfS6/e+//57ltmLFCjFo0CBha2sr1q1bp1e2vb19lp9xL124cEGo1Wq9stPT08Unn3wiFEURvr6+2qHo5cqVE2ZmZqJ9+/YiPT09x7l79uwR5cuXz3JprLi4OOHn5ycOHDigV51leX2Jvaw2Qy+lkiUuLi7L3xaPHj0SKSkpBuc/evRIHDt2TBw7dszgS9WEePFcV6xYUVSpUkVUqVJFmJubC39/f+3fL7ecUqlUolSpUmLgwIFi3bp1RhsCHxoammm5xeXLlxtlKb/XLwMx9uUhRKaMS8zRO0lISAAAgyaey83c1NRUbNq0CWFhYdi7dy9q166Ne/fu4c6dO1i8eDE6d+5s1PszRJs2bRAXF4fVq1drz4L/+++/6Nq1KwoVKmTQhHF16tTBiBEjMg1zj4iIwNSpU3HkyJF3znrXmfoVRcGgQYP0rbI0jo6O2L17d6ZRGcePH0fjxo0RFxenV26ZMmUwZ84ctGjRAvb29oiKitLuO3r0KFatWqVXrp2dHY4ePYqKFSvq7D979izq1KmDZ8+e6ZUrI7tq1arYs2cPChUqhCpVqryxp0Tf4ePAi6GlO3bswH/+8x+dpbOuX7+OihUr6vWcvG3ViZdyOrS5adOmOH78OGbNmoXPPvssx/UqSMzMzLLcb29vD19fXwwfPhwdO3bUK1utViM6Ojrbia6uXbuGSpUqGfR+Wbt2LVavXo1Lly4BeDHMvkuXLnpfHtK6dWsEBgZmumTopTlz5mDfvn1Gmyw0v8tuWdHX6TuqydRMmDDhncqNGzcuR7k1atRAVFQUypUrh4CAANSvXx8BAQEGT7rZtGlTBAYG6izlV7VqVQQHBxu8lN+7js6UNQKFKD/jcHp6J8ZuZMvKPXXqFJYtW4bVq1dDpVLhs88+w/z587XXLc6YMQODBw/OV434efPmoU2bNvD09IS7uzsURcHNmzdRsWJFrFy5Msd50dHR2n8PHjwYQ4YMyXTpwvz58/HDDz/kKDcnM/UbqxH//PlzaDQanX36vmYyMjIyLUkGAJaWlgbNxRAbG6ttDKvVau26wC1btjRoPXOVSpXlutHPnj0zeOipsbPbtGmjva5Q1mz9wIu5EF5eB/6qhw8fvnV5o+y8beZ0QL/rkzUaDWbPnq1dYi4kJERnySlzc3N8//33eg2TnThx4juVM2TJL2N62/vryZMnWLFihV4nO/z9/fH7779n2yCOiIjQruWtr86dOxv1O+Ps2bNvnPW+cePGmD59utHuLzekp6djy5Yter3/Z86cabLXVcuQ08b5uzp27BgSExNx8OBB7Nu3D9OmTcOnn34KHx8fbaO+fv36Ob786ezZszqXs6xZswY1atQwylJ+bJwTZY898ZSt0qVLv/GL9fVrMPM6t1KlSjh//jyaNGmCPn36oFWrVpmuSXrw4AGKFy9uUKNNll27duHChQva5b4aNmyoV46ZmZl2bd030Wfd3dyQlJSEkSNHYt26dXj06FGm4/rWWdaIh3LlymHFihWoUaMGPvroI7Ro0QKjR4/G2rVrMWjQINy/f1+v3M8++wynT5/G0qVLUb16dQAvfoT16dMH1apVQ3h4uF65srNlatGiBapWrYrvv/8e9vb2iI6OhoeHB7p06YKMjAz897//Nfp93rx5E+PHj0dYWFiObrdw4UL88ccf2LJlC4AXvc7+/v7aZZguXLiAkSNHZtv4fJM3TcaoKAouXryI5OTkfPn+zsrZs2dRtWpVveq7fPlyfPnll5g+fTq++OIL7ZwDaWlpWLRoEUaMGIEFCxYgODhY7/oZe/k6a2tr/PXXX9lOinflyhVUrFgRz58/17vOueXChQsICwvD8uXL8eTJk0xzgpBxPXnyBCtXrsTSpUsRFRVlcN7Tp09x8OBB7Nq1C8uWLcOzZ8+QlpaWowxra2tcvnxZuyxb3bp10bRpU3z77bcAXswBUbFixSxPHBORAfJyLD/lb7NmzdLZfvzxRxEUFCQKFy5s0HInsnInTpwobt++rfftC4obN26882YsaWlp4syZM+Lx48cGZ/Xv31+UL19erF+/XtjY2IiwsDDx/fffi5IlS4qVK1fqnXvz5k1RpUoVYWlpKby8vESZMmWEpaWlqFq1qkHLJI0aNUpMnjxZCCHE+vXrhYWFhfD29hZWVlZi1KhReuc+efJEtG7dWiiKIqysrISVlZUwMzMTbdu2NXhuB5nZL6WkpIhbt26Jf/75R2czxPnz50XRokVF06ZNhZWVlfjkk09E+fLlRfHixcWVK1eMUu/XRUVF6XWt70cffSQ2btyo/fv1pZF+/fVXUbNmTaPU8aUzZ86IJk2aCEtLS9G3b1+jZsuk73P80rBhw4SiKMLBwUF7vbCDg4MwMzMTX331lUF1k7F8nZeXl85r43UbNmwQpUuX1rfK0j179kwsXbpU1K5dW5iZmYmPP/5YLF68WDx48EDK/d25c0cMGDBASrap2LVrl+jSpYuwtrYWJUuW1Hv5upfS09PF0aNHxQ8//CCaNGki1Gq1UBRFeHp65jhL5lJ+RJQ99sRTjs2fPx8nT540+jAnQ3O//vrrLHv4FUWBtbU1vL290aZNG+0yZfnJnj17MHPmTO1yX76+vvjqq6/07o2X7auvvkLFihXRq1cvpKeno169ejhy5AhsbW2xdetWBAQE6J1dqlQprFixAgEBAXBwcMDp06fh7e2NX3/9FatXr8a2bdsMqruxRjxk5+jRozh8+DC8vb31mqn5dZcvX9aprz5LWuVm9qVLl9CrVy8cPnxYZ7/4/8vA6ds7rNFo0LhxY4SGhuJ///sfTp06hYyMDFStWhUDBgzQLi1mbPr2Eru4uGDPnj3aodxFixbFiRMn4OnpCeDF8/Thhx9qL78wxPXr1/Hdd99h7dq1aN++PSZNmoSyZcsanJtbDOmJf+no0aNYvXq1dsb0l9etv7yMSB9//PEH2rRpk+3ydXPnzsXvv/+e45nvBw0ahMjISJw4cSLT5RTPnz9H9erVERgY+M7zNeSWI0eOYMmSJVi3bh3Kli2Lrl27YtSoUYiOjoafn59B2efPn8e+fftg97ElRAAAOUpJREFUaWmJTp06wcnJCQ8fPsTkyZOxcOFClC5dGufPnzfSIzENN2/exLJly7Q95E+ePMG6devQoUMHvfJOnDiBffv2ITIyEocOHcKzZ89QsmRJBAQEIDAwEIGBgdrPp5zo27cvzp07p13Kb/ny5bhz54720qzffvsNs2bNwokTJ/SqNxFlIy/PIJBpunr1qsGzpsvIDQgIEA4ODsLOzk5UrVpVVKlSRajVauHo6Chq1KghnJycRKFChcRff/1lxFobbu7cucLCwkJ06dJFzJ49W8yePVt8+umnwtLSUsydO9co9/H333+L//3vf5lmh9ZXiRIlxIkTJ4QQQmzatEm4ubmJixcvim+++UbUrl3boLra2dlpRwmUKFFCHDt2TAghxLVr14SdnZ1B2SRf7dq1Rb169cS2bdvEmTNnRFRUlM5mCGdnZ3Hp0iUj1fTd6NtLnN3KEC/FxMQIlUplSNXEgwcPxMCBA4WVlZVo0KCBOH78uEF5ecXQnnhZ6tWrJ7755ptsj3/zzTeiXr16Oc6NjY0Vbm5uwt3dXUydOlVERESI33//Xfzwww/C3d1duLm5idjYWEOqbnTly5cXHh4eIiQkRPz999/a/RYWFjp/62PLli3CyspKO8t9mTJlxN69e4Wzs7MICAgQW7ZsMbT6JmXt2rWiUaNGwtbWVnzyySciIiJCpKSkGPxcv1wJKCgoSCxevFhcvnw5Uxl9RjPev39f1K1bVyiKIuzt7TONMmnQoIEYM2aM3vUmoqxxYjvKsf/+979SerMNzX3Zy75s2TLt5GcJCQno1asX6tatiz59+iAoKAhDhw7Fjh07jFVtg4WGhmLmzJkYOHCgdt/gwYNRp04dTJ48WWd/Tl27dg3t2rXDuXPndK6TfzliQd+er4cPH8LFxQUAsG3bNnTs2BE+Pj7o1auXwb1HXl5euHHjBjw8PODn54d169ahevXq2LJlC5ycnAzK3r9/P6ZPn64d8VC+fHmMGDECH330kUG5V69exaxZs7S5fn5+GDJkSLYzZmdn6NCh71z2p59+yjfZr4qKisKpU6fg6+urd0Z2PvvsM+265fldyZIl8ddff6FcuXJZHo+OjkbJkiX1yk5MTMT06dPx008/wdvbG1u2bNF7vevc8LbPhH///Vfv7MuXL2Ps2LFYtGhRpkkv4+Pj8eWXX2LSpEk5fi8CwJkzZ/DLL79ke7x79+6YPXt2jnNfXWM8JCRE53O5SZMmBq8xLsOVK1fQpUsXBAYGonz58kbNnjx5Mvr164fJkyfjl19+wfDhw9GvXz9s2LAB9erVM+p9mYKgoCCMHDkSGzZsgL29vdFyY2Jisv08io2NxeTJk7FkyZIcz8VQtGhRHDx4EPHx8VCr1ZnmIlq/fj3UarXe9SairLERT9l6fakoIQRiY2Px4MEDLFiwIN/l/vjjj9i1a5fODzkHBweMHz8ejRs3xpAhQzB27Nh892M3ISEBTZs2zbS/cePG2iVb9DVkyBCULl0au3fvhpeXF44fP45Hjx5h2LBhBs1+XLx4cZw/fx6urq7Yvn279v8tKSkp0xd4TvXo0QNnz55F/fr1ERISghYtWmDu3LlIS0szqHG5cuVK9OjRA+3bt8fgwYMhhMDhw4fx8ccfIzw8HEFBQXrl7tixA61bt0blypVRp04dbe6iRYuwZcsWNGrU6J2zli1bhgoVKsDCwuKNkxPqM5PzmTNn3qmcobNE+/n54eHDhwZlZCc1NRVLlizBrl278MEHH8DOzk7nuD6vj/bt27/xuL5LDzZv3hxjx45FixYtshwyPWHCBLRo0UKv7DJlyuDp06cYNGgQPv30UyiKorMqxUuVKlXSK9/Y3mUFgFKlSumV/eOPP8Ld3T3LVSscHR3h7u6OH3/8ET///HOOs7Nb0eIlS0vLt04gmh0PDw9s27YNT548wZUrVyCEQNmyZVGoUCG98mS7fv06wsPD8eWXX+L58+f49NNP0bVrV6PMKh8TE4Ply5dDrVZj8ODBGDlyJGbNmvVeNuABoGfPnliwYAH279+P7t27o3PnzkZ5Xbi4uKBr167YuXMnLC0tMXr0aAwcOBDjx4/H9OnT4e/vn+MJPF/l6OiY5f78eAkjUUHAa+IpW+PHj9f5gjYzM0PRokUREBBgUC+brFy1Wp3l9diRkZFo1aoVnj59imvXrqFy5cra9enzg65du6Jy5coYMWKEzv7p06fj1KlTWL16td7Zzs7O2Lt3LypVqgRHR0ccP34c5cqVw969ezFs2LB3bti9bvz48Zg1axZcXV2RlJSES5cuQaVSISwsDIsXL87R+vNvc/PmTZw8eRJlypTBf/7zH71zypcvjy+++CLTbOA//fQTFi9ejJiYGL1yq1SpgiZNmmTqHR49ejR27tyZo3XRzczMEBsbi2LFisHLywsnTpwweA3fl6Kjo+Hv72/wSZa32bt3L7799ltMmTIFFStWzNQIMmRZycDAwGyPKYqCvXv35jhT1jrE9+7dQ+XKlWFlZYWBA/9fe3ceV3P6/g/89T7VUZYkS2TaF1u2scsWPkWDaOY7lkFJDDOTLIWY7M1YsxSTvQz62CrTMJhPyKghVPYSURlLQkJFne7fH/0643SKzvtsnbqej0ePx3S/z+c61+lz1Lne931f9w+wtbUFx3FISUlBcHAwiouLkZSUxGvG9cNz18vf7Cn7vrqePqForVu3xq+//opu3bpVeP3KlSsYN24cUlNTZY7do0cPjBkzptITBAIDA3HgwAFcvHhR5tia7PTp09i1axciIiJQWFgIHx8feHp6wtbWlle8D3/vAaUnOSQnJ8PKykqRaWuUgoICHDx4ELt27cLFixfh5OSEY8eOITk5GXZ2drxifvfdd4iOjsbo0aNx4sQJ3L59G05OTigsLMTixYvRv39/Bb8KQohSqWURPyFKMG7cOGZhYcEiIiJYVlYWe/jwIYuIiGCWlpZs/PjxjDHGwsPDWZcuXdScqaTly5ezhg0bMmdnZ7Z8+XK2fPly9sUXXzADAwO2fPly8T75jRs3yhzbwMBA3BHb0tKSnT59mjHG2N27d5menp5ceR86dIgFBgZKdHYPDQ1lUVFRcsWtKjs7O5aZmVnlxwuFwgr3AKalpcm1N7lOnToV7tNOTU2VOa6hoSG7cOECY6x0/2J2djbvvMoTCATieBYWFiwnJ0dhsT9Utq9VIBBIfJWN1Sbp6enMyclJ/PrLfgZOTk4SneplperTJ+QVExPD2rRpw169eiV1LTc3l7Vt25adO3eOV2xdXd2PvtYHDx7w/l0XGhrK9PT02ObNm1lRUZF4vKioiAUHBzM9PT22e/duXrFrgtzcXLZ582bWpUsXxnEca9++Pa84HMexM2fOsKtXr7KrV6+yevXqsWPHjom/L/uqrdLS0ti8efOYsbEx09fXZ2PHjmVHjhyROY6pqSn7888/GWOlPYg4jmPe3t4KzpYQoipUxJNKCQQC9vTpU6nxnJwcuT6MKyvu69evmaenp/i4LIFAwIRCIZsyZQp78+YNY6z0CKakpCTez6EM5ubmVfric+RQnz59WGRkJGOMsbFjx7IhQ4aw8+fPs4kTJ7J27dop+JVIk7XQlkX5I7s+xcrKioWEhEiNh4SEMGtra955fPbZZ+zgwYNS4wcOHGAmJiYyxZoyZQoTCoXM3NycCQQCZmpqyiwsLCr8kpUybxB86OzZsx/9qo2eP3/OLl68yC5evMieP3+u7nRUbvjw4SwwMLDS6xs3bmQjR47kFdvIyIjFxMRUev1///sfMzIy4hWbMeUeX6dJXFxcWHR0NBOJRBVeT0pKYl5eXrxil93cKrvR9eFXbbwB+PbtW/bdd98xY2Nj1rRpUzZ27Fj27NkzJhKJ2G+//cZcXFyYUCiUOa62tjb7559/xN/r6emx69evKzJ1QogK0XJ6UqnyS9zKPHr0CFZWVjI3P1F23DJv3rxBeno6GGOwsrKq1Q1VTp48ibdv38LV1RXp6ekYNmwYUlJS0LhxYxw4cAADBw5U6vM3aNAAV69e5dVUStGxf/nlF8ycORMeHh7o3bs3OI7D+fPnERoaio0bN+Lbb7/llceyZcuwfv16zJ8/XyLuqlWrMGfOHPz4448yxTtx4gTu3r2LGTNmYNmyZZU2NvL29pYp7tSpU7Fnzx60aNECmZmZ+OyzzypdWp+eni5TbFK9REREYMmSJRXuk1cHMzMznDhxotKGaCkpKXB0dERmZqbMsb/++msUFRUhMjKywusuLi4QCoU4dOiQzLHLXLx4EeHh4bhz5w4AxRxfp2mcnJwQExODZs2awd3dHZMmTVLYMYYZGRlVepyZmZlCnq+68/X1xZYtW/DNN99AV1cX4eHhGDBggMR7ODs7W+oz1KdoaWnhyZMnaNq0KYDSv6HXrl2DhYWFQvMnhKgGNbYjUso6CXMchx07dkgUwSKRCOfOneO1d11ZccurX79+tWnopEj6+vpITk6WqSB2cnIS/7elpSVu3bqFFy9eoFGjRgppSKRJpk+fjubNm2PdunU4ePAggNJ98gcOHICLiwvvuP7+/mjQoAHWrVsHPz8/AICxsTGWLFmCGTNmyByvrMnhlStX4O3trbDuxNu2bYOrq6v4BsGUKVMU2vn4Q7m5udi5c6dEt34PD49KGx8R2W3fvl3coMrb2xs9evQQ97pITU3FhAkT1J2i2NOnTz/aIE5bWxvPnj3jFdvPzw+9evXCV199hblz54q7b6ekpGD16tU4efIk4uPjecXOz8+Hr68voqKiUFRUhEGDBiEoKAhNmjThFU+TnTx5Eg8fPsTu3bsRFhaGVatWwd7eHp6envi///s/6Onp8Y5dW4rzqoqIiMDOnTsxZswYAMD48eNhb28PkUgkvvEqawEPlDYRdnd3R506dQAAhYWFmDZtmlSD0IiICDlfASFEFWgmnkgpuyubkZEhNVsnFAphbm6OZcuWoUePHtUibm2hzFltZakuM/HFxcUICAiAh4cHTExMFJ5LmdevX4tzq84mTZqETZs2fTLPhw8fwtjYWKKR2qdcvnwZTk5O0NPTQ/fu3cEYw+XLl1FQUIBTp07h888/lzf9Wm/t2rVYsGABOnToIG7IuHDhQgQGBsLLywvff/99tSo0rayssHbtWowaNarC6xEREfDx8eG9AuT333+Hh4cHnj9/LjHeuHFj7NixAyNGjOAV98MZUT09Pezfv19qRrS2OnPmDHbt2oXIyEhoaWlhzJgx8PDw4PX3+9y5cxWON2zYENbW1lJFZk0nFApx//59tGzZUjymp6eHO3fuyPX3S1lNPAkh6kFFPKmUg4MDIiIiFH7kjbLi1nRVLVpdXV0RGhoKfX39Tx6fpew77tWliAdKV2jcuHED5ubmCs8FKF3emJqaCo7j0KpVK/GSRU3GZ/VH3759YW1tje3bt0Nbu3SxV3FxMTw9PZGenl7pB3ZSdW3atIGvry88PDxw9uxZDBw4EAMHDsThw4dhYGCg7vSkeHl54ezZs7h06VKFx+11794dDg4OnzxP/mMKCgrEW1EYY7C1tYWjoyPq1q3LO6aVlRUCAgLEM6IJCQmwt7dHYWGh0k950BSvX7/G/v37sWDBArx69QrFxcUyx/jYTUItLS1Mnz4d69at++hqjpqk/LJ3gJa+E0Kk0XJ6UqkzZ85oVFxSqmHDhuKl8vr6+rVu2XxlBg8ejLNnz8Ld3V2hcfPy8vD9998jPDwcJSUlAEo/hI0ePRqbN2/W6CXkfO7xXr58WaKAB0qXS8+dOxddu3ZVZHq1VkZGBgYPHgwAGDBgAHR0dBAQEFAtC3gA+PHHHxEREQFbW1v88MMPaNWqFTiOw+3bt7F582aIRCIsXLhQrufQ09OrcKZfnv4AWVlZ6Nu3r/j77t27Q1tbG48ePVLqih5NkZ6ejtDQUISGhuLVq1fi96SsXr58WeF4bm4uEhIS4Ovri+bNm2PBggXypKsxyi97Bype+k7L3gmp3aiIJxJmz56N5cuXo169epg9e/ZHHxsYGKj2uETah0vhQkND1ZcIT/fv36/SbMPWrVtlOmN76NCh8PPzw40bN9ClSxepJZp8l9x6enoiOTkZx44dQ69evcBxHOLj4+Ht7Y0pU6aI99/XFvr6+sjMzJTqb5GVlVXttxloisLCQokZbaFQWK1XfhgZGSE+Ph7Tp0+Hn5+f+OYQx3FwcnLCli1bZPq3XF5ZfwChUIgZM2YorD+ASCSCUCiUGNPW1uY121xTFBQU4NChQ9i9ezfOnTsHU1NTeHp6YtKkSbxvbFR2o7Nhw4YwMzODUCjEggULak0R7+bmJjU2fvx4NWRCCKnOqIgnEpKSklBUVAQASExMVNgs7odxk5KSKn0czRpXjs/PZuDAgYiIiJCaocvLy8PIkSNx+vRpXrkoq9AGAGtra/Tr1w+TJ0/GV199JbX8tsy4ceNkijt9+nQAFd8k4jgOIpFIpnhljh07hpMnT6JPnz7iMScnJ2zfvl3cpK42GT16NCZPnoy1a9dKdOv39fXF2LFj1Z1ejfFhc9Di4mKEhoZK7YPn01hRWczMzHD8+HG8fPlSvOTdxsZG7m1V5fsDREVFKaw/AM2I/is+Ph67d+/GwYMH8f79e4wcORInT57kPfsui44dO1a5g31NQHvSCSFVQXviCdEQfPaXV3acX3Z2Nlq2bCm+sSIrLS2tKhXafNy4cQO7du3Cvn378O7dO3FR2L17d4U9hyKZmpri2LFjaN++vcT4tWvX4OzsjIcPH6opM/nxec+9f/8evr6+CAkJEc9Y6ujoYPr06Vi5cqVEQUT4MTc3/+RNPY7jasVRgcrsD0CNwP4lEAjQsWNHTJ48Gd98841Ke9rEx8dj/PjxteL9TAghVUVFPKmUh4cHNm7cKLUE9u3bt/Dy8sKuXbvUlFntdP78eXTr1q1KRVDZ/s9OnTrh9OnTMDQ0FF8TiUQ4ceIEtm7digcPHvDKRRWFdnFxMaKjoxEaGoo//vgDNjY2mDx5MiZMmFCtlg5v27YNhw4dEp/BDgBPnjyBm5sbXF1deZ8/Xx3waWxXJj8/H/fu3QNjDNbW1nI1GCOkMnXr1kVKSgpMTU0BAHXq1MG5c+folBMFS0xM/OjJEo8fP0ZAQACCg4MV+rzZ2dkYM2YMLC0tsWPHDoXGJoQQTUZFPKmUlpYWHj9+LDWLm5OTg+bNm/PeFzhq1KgKZ5E4joOuri6sra0xbtw48Xm/NV1lPQI+/Hm4uLhIFOKfIhAIxD/jiv6J6+npISgoCB4eHvyS/v9UUWi/e/cOW7ZsgZ+fH96/fw8dHR2MHj0aq1atEhfNVRUTE4OYmBhkZ2eLm9CVkeWmVOfOnSXew2lpaXj37p24kMjMzESdOnVgY2ODxMREmXKsTvjMxL969QoikUjq/frixQtoa2tDX19f0WmSWqz8aiNNPIpTU9y6dQtnzpyBjo4Ovv76axgYGCAnJwcBAQEICQmBhYUFbt26JXPc8r9Py7x69QoPHz5EmzZtcOrUKV5noxNCSE1FRTyRkpeXB8YYGjVqhLS0NIliTCQSITo6GvPnz8ejR494xXd3d0dUVBQMDAzQpUsXMMaQlJSE3NxcODo64urVq3jw4AFiYmJgb2+vqJdVbTk4OCAxMREikQitWrUCYwxpaWnQ0tJC69atxceWnT9/Hm3btq1SzIyMDDDGYGlpiYSEBIn/D4VCIZo1a6bQI5IUWWiXuXz5Mnbt2oX//ve/qFevHtzc3DB58mQ8evQIixYtwuvXr5GQkFDleEuXLsWyZcvQtWtXtGjRQupDY2RkpEyxqmrx4sVVfmx1k5WVBWNjY5neK0OHDsXw4cPx3XffSYyHhITgt99+w/HjxxWdZq3j7OyM8PBwcUOwgIAAfP/99+Ll48+fP0ffvn15FVSaRiAQYMWKFeL+APPmzYOvr2+17g+giX7//Xd8+eWX4i1YlpaW2L59O77++mvY2dlhzpw5GDZsGK/Ylf0+1dfXR+vWreHo6EhH+hFCSDlUxBMpH87iVoTjOCxdupT3kUDz589HXl4egoODxefDlpSUwNvbGw0aNEBAQACmTZuGmzdv4vz587yeQ5Ns2LABf/31F3bv3i2epczLy8PkyZPRp08fTJkyBePGjUNBQQFOnjyp5mwlKbrQBkobz+3evRupqalwdnaGp6cnnJ2dJc4Svnv3Llq3bi3TapAWLVpg9erVvDtVyys8PBwjRoyQ6oqvKq6urlV+rDyNugwNDREXF4c2bdpIjKekpMDe3h7Pnz/nHZuUKr9Kqvy2h6dPn8LY2Jh3s0ZNQv0BVKNXr17o3r07AgICsG3bNvj4+MDGxgbbt29Hv3791J0eIYTUOlTEEymxsbFgjGHgwIE4cuSIxLJYoVAIMzMzGBsb847ftGlTxMXFwdbWVmL8zp076N27N3JycnD9+nX07dsXubm5vJ9HU7Rs2RJ//vmn1Cz7zZs34ejoiH/++QeJiYlwdHRETk6OzPHv3buHDRs24Pbt2+A4Dm3atIG3tzesrKx456ysQhsAbGxs4OHhgUmTJqF58+YVPub9+/cIDw+v8CieyjRu3BgJCQlyvW55yLO/XBGq2qQLkK9RV7169XDhwgWpRn/Xr19Hjx49kJ+fzzs2KfWpJeS1qYgnqmFgYICEhATY2tqiuLgYurq6iI6OxtChQ+WO/fLlS+zduxdubm5S221evXqFPXv2VHiNEEJqMzpijkjp378/gNJjxExMTCQKM0UoLi5GSkqKVBGfkpIi/tCpq6tba46be/XqFbKzs6WK+GfPniEvLw9A6Qeo9+/fyxz75MmTGDFiBDp16gR7e3swxhAfH4927dohOjoa//nPf3jl/Msvv3yy0DY1NcXOnTtljv3nn3/C1NRU6n3HGENWVhZMTU0hFAplKuCB0vPc9+/fD39/f5lzUgR13y9VVQftbt26Ydu2bQgKCpIYDwkJQZcuXVSSAyFEsfLy8sTbNbS1taGnpyf1N5yv4OBgXLt2DV5eXlLXGjZsiL/++gt5eXm8V/8RQkhNREU8qZSZmRmA0i7TmZmZUkVkhw4deMWdMGECJk+ejAULFqBbt27gOA4JCQn46aefMHHiRAClqwHatWsn3wvQEC4uLvDw8MC6deskfh4+Pj4YOXIkAIhnQGQ1f/58zJo1CytXrpQanzdvHu8iXlmFNgBYWVlV2FDxxYsXsLCwkGl28cOmgSUlJdi2bRv+97//oUOHDtDR0ZF4bEXnxxPZBQQEYPDgwbh69SoGDRoEoLSh4KVLl3Dq1Ck1Z1czcBwndZOzttz0LI/6A6jOrVu38OTJEwClv+tTU1Px9u1bicfw+Vxw5MgRrFu3rtLr3377LXx8fKiIJ4SQD9ByelKpZ8+eYdKkSfjjjz8qvM53qaZIJMLKlSsRHByMp0+fAgCMjIzg5eWFefPmQUtLC5mZmRAIBPjss894568p3rx5g1mzZmHPnj3ipefa2tpwc3PD+vXrUa9ePSQnJwMoPTJOFrq6urh+/TpsbGwkxu/cuYMOHTqgsLCQV86VnVzw/PlzNGvWTK5lvJWdbZ+RkYG2bdtKfWj8GAcHhyo/9syZM1V+LB/VrWv24cOHcfDgwQpv0MnbUT85ORlr1qxBcnIy9PT00KFDB/j5+Um9Dwk/AoEAQ4cOFR83GR0djYEDB4r7Lbx79w4nTpyoFcvpqT+AapT1yqnoI2PZOMdxvH7ODRo0wM2bN8Wne5SXmZkJOzs78co0QgghNBNPPmLmzJl4+fIlLly4AAcHB0RGRuLp06dYsWLFR++af4qWlhYWLlyIhQsXiv8ol9/rVtkf85qofv362L59O9avX4/09HQwxmBlZSXutgzIXryXadq0KZKTk6WKp+TkZLmO66ns3t+bN2+gq6vLK2bZrDnHcVi0aJHEueIikQgXL16U+eeg7MJcU23atAkLFy6Em5sbjh49ikmTJuHevXu4dOkSvv/+e7njd+rUCfv27VNApqQiEydOlJh5Hz9+fIWPqQ3K/y6ieQnluH//vtJia2lp4dGjR5X+3X/06JHCt/URQoimoyKeVOr06dM4evQounXrBoFAADMzM/znP/+Bvr4+fv75Z3zxxRdyPwc1qvlX/fr1eW9RqMyUKVMwdepUpKeno3fv3uKj6latWoU5c+bIHE8ZhXaZpKQkAKUfwq9fvw6hUCi+JhQK0bFjR/j4+PCKDQAeHh7YuHEjGjRoIDH+9u1beHl5yXROvKbbsmULtm3bhrFjxyIsLAxz586FpaUlFi1ahBcvXsgcT5YZMvo3L7/Q0FB1p0BqmbLtdcrQuXNnREVFoWfPnhVej4yMROfOnZX2/IQQoomoiCeVevv2rXi21tDQEM+ePYOtrS3at28v13Lbp0+fwsfHBzExMcjOzpaaOaltyx7fvn2LlStXin8eJSUlEtflORrJ398fDRo0wLp16+Dn5wcAMDY2xpIlS3idm6zMQrts1tzd3R1BQUFSxba8wsLCsHLlSqm4BQUF2LNnj9KLeDMzM6l9+OqSmZmJ3r17AwD09PTw+vVrAKX9Knr27Ing4GCZ4hkYGHxyT7Y8y22JpMq2s9RG1B9ANVavXg0vLy/o6ekBAM6dO4cePXqIt3S8fv0a8+bNw5YtW2SO/cMPP2DMmDH47LPPMH36dPGZ8CKRCFu2bMH69euxf/9+xb0YQgipAaiIJ5Vq1aoVUlNTYW5ujk6dOmHr1q0wNzdHSEgIWrRowTuuu7s7MjMz4e/vjxYtWtT6D1yenp6IjY3FhAkTFP7z4DgOs2bNwqxZs8SFmjzFsbIL7eLiYuzduxc+Pj6ws7NTSMy8vDwwxsAYw+vXryWW+4tEIhw/flwhxdDly5fFx/i1bt0aXbt2lbh+48YNuZ9DUZo3b47nz5/DzMwMZmZmuHDhAjp27Ij79+/zWo5M2xZUi5aM/4sxBnd3d3ExWVhYiGnTpkn0ByDy8/Pzg7u7u7iIHzZsmETvgfz8fGzdupVXEf/ll19i7ty5mDFjBhYuXAhLS0twHId79+7hzZs38PX1xVdffaXQ10MIIZqOGtuRSu3btw9FRUVwd3dHUlISnJyckJOTA6FQiLCwMIwePZpX3AYNGuCvv/7ivey6pjEwMMCxY8dgb2+v7lSqpOyM4OTkZIUV2h+ysrJCREQEOnbsqJB4ZQ2ZKsNxHJYuXcq78/HDhw8xduxYxMXFiTti5+bmonfv3ggPD4eJiQmvuMrk6ekJExMTLF68GCEhIZg9ezbs7e1x+fJluLq68joakKhOZc0fayN3d/cq3fhU1RGLNVX591z5Rp2KaCCYkJCAffv24e7du2CMwdbWFuPGjUP37t0V8hoIIaQmoSKeVFl+fj5SUlJgamqKJk2a8I7Ttm1b7Nu3j/a4/X8WFhY4fvw42rRpo/DYnTt3rvADLsdx0NXVhbW1Ndzd3WXq4g4ovtD+0O7du3Ho0CHs3bsXhoaGcseLjY0FYwwDBw7EkSNHJGIKhUKYmZnB2NiYd3xHR0fk5eUhLCwMrVq1AgCkpqbCw8MD9erVq5bHqpWUlKCkpATa2qWLsQ4ePIjz58/D2toa06ZNk9gmwZeij6Yk/xIIBAgLCxMfq1aZESNGqCgjUtOpoognhBBSdVTEEwkfnqv9KXzP1T516hTWrVsnXp5f2+3duxdHjx5FWFiYRKM4RfDz88Mvv/yC9u3bo3v37mCM4fLly7h27Rrc3d1x69YtxMTEICIiAi4uLlWOq+hC+0OdO3fG3bt3UVRUBDMzM/Gy2DJ8+zFkZGTAxMRE4V2O9fT0EB8fL3VTKjExEfb29igoKFDo8ylCZmYmTExMpG7wMMaQlZUl1+kQyjqakvyrKu/h2tJ/gPoDqIYyi3hl7rcnhJCaivbEEwlljcs+RZ5926NHj0Z+fj6srKxQt25dqWZffLpja7J169bh3r17MDIygrm5udTPQ54mgjk5OZgzZw78/f0lxlesWIGMjAycOnUKixcvxvLly2Uq4jdt2oS7d+/C2NhYoYU2AIwcOZL3//ZjyrorK3qG2NTUFEVFRVLjxcXFaNmyJa+YymZhYVFh4fPixQtYWFjIVfwp62hKIomW05eieQjV2bFjh/jo0+LiYoSGhopX5ZX1XOFDmfvtCSGkpqIinkhQRYOqDRs2KP05NImyilagdJn0lStXpMbHjBmDLl26YPv27Rg7dqzMqyqUmfPixYuVEldZM8Rls0ibN29Gly5dwHEcLl++DG9vb6xdu1aelJWmrFN8eW/evJFo/MeHKo6mrO1qezNQonqmpqbYvn27+PvmzZvj119/lXoMH+VvxNCNGUII+TQq4onKubm5qTuFakVZRSsA6OrqIj4+HtbW1hLj8fHx4mKtpKREvGyxqpSZM1DaGO7w4cO4d+8efH19YWhoiMTERBgZGfGe3VbWDLG7uzvy8/PRo0cP8R7z4uJiaGtrw8PDAx4eHuLHqnuVSdl2GY7j4O/vL7F9QyQS4eLFi3I3nFTW0ZTkX1TkSDp58iT1B1CyBw8eqDsFQgghH6AinqiFSCRCVFSU+Eiutm3bYsSIEeLzYYlieHl5Ydq0abhy5Qq6desGjuOQkJCAHTt2YMGCBQBKPwDzaTKojEIbAK5du4bBgwejYcOGePDgAaZMmQJDQ0NERkYiIyMDe/bs4RVXWTPEmrSypGy7DGMM169fl2hgJxQK0bFjR/j4+Mj1HMo6mpL8y83NTbz0mHz6xnBt6Q+gTBcvXsSLFy8wdOhQ8diePXuwePFivH37FiNHjkRQUJDMN4QJIYTwQ43tiMrdvXsXzs7O+Oeff9CqVSswxnDnzh2YmJjg2LFjsLKyUneKSmdoaIg7d+6gSZMmaNSo0UeXx8o7e7tv3z4EBwcjNTUVQGmR5eXlhXHjxgEACgoKxN3qq6p8oZ2amgpLS0v4+/vLVWgDwODBg/H5559j9erVEs2T4uPjMW7cON4zQvr6+rh27RrMzc1hbm6Offv2wd7eHvfv30e7du2Qn5/PO2dNM2nSJGzcuBH6+voKj62soykJqQgdt6caQ4YMgYODA+bNmwcAuH79Oj7//HO4u7ujTZs2WLNmDb799lssWbJE5tgCgQArVqwQ77efN28efH19JfbbL1q0iG7EEELIB6iIJyrn7OwMxhj27dsn7mz+/PlzjB8/HgKBAMeOHVNzhsoXFhaGMWPGoE6dOggLC/voY6vj9gNlFdoA0LBhQyQmJsLKykoidkZGBlq1aoXCwkJecbt164YVK1bAyckJI0eOFM/Ab9q0SbyigI/MzMyPXpen07sqPHz4EBzHKaUJH2MMBQUFCjmakvxLIBB8cl88x3EoLi5WUUbqQ93pVaNFixaIjo5G165dAQALFy5EbGwszp8/DwA4dOgQFi9ejFu3bskc29zcvEp9Hu7fvy9zbEIIqaloOT1RudjYWFy4cEHiaLLGjRtj5cqVsLe3V2NmqvNhYa7sIr1s2Xt6ejp8fHwUsuz90qVL2Lp1q9R4y5Yt8eTJE7ny1dXVRV5entR4amoqmjZtyjvuzJkz8fjxYwCle/qdnJywd+9e8QwxX5/6AFodZ49KSkrEvQDevHkDoPTIqDlz5mDhwoVyH8O3c+dOrF+/HmlpaQAAGxsbzJw5E56ennLnToCIiIhK33Px8fEICgqqNfvma8vrVLeXL1/CyMhI/H1sbCyGDBki/r5bt27IysriFZv22xNCiOyoiCcqV6dOnQqPo3nz5o3EHt3aJjs7G9nZ2SgpKZEY53v0GSC97N3T01Mh+8uVVWgDgIuLC5YtW4aDBw8CKJ1RzMzMxPz58/Hll1/yjvvNN9+I/7tTp0548OCBQmaIyx/LWFRUhKSkJAQGBiIgIIB3XGVauHAhdu7cKb5xxhhDXFwclixZgsLCQrny9vf3x/r16+Hl5YVevXoBAP7++2/MmjULDx48wIoVKxT1Mmqtik6HSElJgZ+fH6Kjo/HNN99g+fLlqk9MDag/gGoYGRnh/v37MDExwfv375GYmIilS5eKr79+/VrqeNSqov32hBDCAyNExSZMmMDatWvHLly4wEpKSlhJSQn7+++/mZ2dHXNzc1N3eip3+fJl1q5dOyYQCBjHcRJfAoFArtiDBg1ivr6+jDHG6tevz+7du8cYYywuLo6ZmZnxjjtlyhQ2cuRI9v79e1a/fn2Wnp7OMjIyWOfOnZm3t7dcOb969YrZ29szAwMDpqWlxUxMTJiOjg7r168fe/PmjVyxd+zYwdq1a8eEQiETCoWsXbt2bPv27XLFrMzvv//O+vfvr5TY8mrRogU7evSo1HhUVBQzNjaWK3bjxo3Z/v37pcb379/PGjduLFdsIu2ff/5hnp6eTEdHhw0bNoxdv35d3SmRGmjq1KmsV69e7Ny5c2z27NmscePG7N27d+Lre/fuZV27duUV28nJia1cuVL8/bVr15i2tjbz9PRk69atY82bN2eLFy+W9yUQQkiNQjPxROU2bdoENzc39OrVS3znvqioCC4uLhrV6VtRJk2aBFtbW+zcuRNGRkYKPQNaWcve165dC2dnZzRr1gwFBQXo378/njx5gl69esk9+6yvr4/z58/j9OnTSExMRElJCT7//HMMHjxYrriqniG2tbXFpUuXFBpTUV68eIHWrVtLjbdu3VruRooikUi8b/ZDXbp0qRV7tFXl1atX+OmnnxAUFIROnTohJiYGffv2VXdaKkf9AVRjxYoVcHV1Rf/+/VG/fn2EhYVJrJzbtWsXHB0decW+evWqxO/f//73v+jRo4f4XHoTExMsXryYV9M8QgipqaixHVGbu3fv4vbt22CMoW3btlJnmdcWDRo0QFJSklJev5GREU6cOIHOnTtLNIk7deoUJk+ezHsPYxlFF9rK1KRJEwQFBWHs2LES4+Hh4fDy8kJOTg6vuOW3FTDG8PjxYyxZsgQpKSlITk7mm7LS9OjRAz169MCmTZskxr28vHDp0iVcuHCBd2wvLy/o6OggMDBQYtzHxwcFBQXYvHkz79ik1OrVq7Fq1So0b94cP/30E1xcXNSdktpERUVVqT9AQUGBijOrmV69eoX69etLHQf74sUL1K9fn9eWOF1dXaSlpcHExAQA0KdPHwwZMgQ//vgjgNI98+3bt69wGx4hhNRWVMQTlZg9e3aVH1v+w39NN3LkSEyYMEGu/d6VmTp1Kp49e4aDBw/C0NAQ165dg5aWFkaOHIl+/fpV25UPMTExWL9+PW7fvg2O49C6dWvMnDlTrpsEjRo1QkJCAmxsbCTG79y5g+7duyM3N5dX3IpmAhljMDExQXh4OHr37s03ZaWJjY3FF198AVNTU/Tq1QscxyE+Ph5ZWVk4fvy4zDO6H/77Li4uRmhoKExNTdGzZ08AwIULF5CVlYWJEyciKChIoa+lNhIIBNDT08PgwYOliqkPRUREqDCr6qOi/gDV/ZSI2szMzAy//vor+vXrh/fv38PAwADR0dEYNGgQgNLj7Pr37y/3KiFCCKlJqIgnKuHg4FClx3Ech9OnTys5m+olJycHbm5u6N69O+zs7KSaA40YMYJ37Ly8PDg7O+PmzZt4/fo1jI2N8eTJE/Ts2RN//PEH6tWrxzu2MgptAAgODsasWbPw1VdfiZe9X7hwAYcPH0ZgYCB++OEHXnGVNUMcGxsr8b1AIEDTpk1hbW0Nbe3quWMpMzMT2tra2Lx5M1JSUsSrYb777jsUFxfLXPDQv2/Vcnd3r9K2m927d6sgm+rj0aNHWLx4McLCwuDk5ISff/4ZdnZ26k6LfMK3336L69evY9WqVYiKikJYWBgePXokntXft28fNmzYUG23JxFCiDpQEU+Imv3222+YMGFChUsFOY5TyBFlZ86cwZUrVxS27F1ZhTZQul/fz89PKsbmzZsREBCAR48eVTmWKmaIf/75ZxgZGcHDw0NifNeuXXj27BnmzZvHK64yVXa29vPnz9GsWbNqeSweIZUp3x9g1apVtbI/gKZ69uwZXF1dERcXJ95vP2rUKPH1QYMGoWfPntX2tA9CCFEHKuIJUTNzc3MMGzYM/v7+EufwKkpMTAxiYmIqPL5u165dvGIqstAur7IeAWlpaejcubP4XPOqUMUMsbm5Ofbv3y+1bP7ixYsYM2YM7t+/zyuuMgkEAjx58kSqiM/IyEDbtm3x9u1bNWVGqsLV1fWTj+E4DkeOHFFBNupF/QFqDmXstyeEkJqqeq71JKQWef78OWbNmqWUAn7p0qVYtmwZunbtihYtWiis831eXh6GDBkiNe7o6Cj3zPOIESMQGRkJX19fifGjR49i+PDhMsU6c+aMXLlUxZMnT9CiRQup8aZNm+Lx48dKf35ZlK1M4DgOixYtQt26dcXXRCIRLl68iE6dOqkpO1JVDRs2VHcK1cb8+fOhp6cHa2trhIWFISwsrMLH1db+AJqksve1oaGhijMhhJDqj4p4QtTM1dUVZ86cgZWVlcJjh4SEIDQ0FBMmTFBoXEUW2uW1adMGAQEBOHv2rMRS/bi4OMyZM0eio/qMGTPkei5FMDExQVxcHCwsLCTG4+LiYGxsrKasKpaUlASgtPHe9evXJWa2hEIhOnbsCB8fH3WlR6qotu11/5iJEycq9FhOQgghRBPQcnpC1CwgIAAbNmzAF198gfbt20s1tpOnUG3cuDESEhIUfoNgxYoVWLt2Lezt7SsstPX19cWPlTX/8sVwZTiOQ3p6ukyxlWHVqlVYs2YN1qxZg4EDBwIo3cIwd+5czJkzB35+fmrOUNqkSZOwceNGif+fCCGEEEKIZqAinhA1+1jRKm+hOm/ePNSvXx/+/v68Y1RE0wptZWKMYf78+di0aRPev38PoPTc43nz5mHRokVqzo6Qmo36AxBCCKmNqIgnpAbz9vbGnj170KFDB3To0EFqlr/8cWvVTdmvJ01YLvvmzRvcvn0benp6sLGxQZ06ddSdEiE13qRJk6r0ONqCQAghpCahIp6QGuxj3dkVdWa3MgrtPXv2YM2aNUhLSwMA2NrawtfXV+F7+wkhhBBCCNE01NiOEDVjjOHw4cM4c+ZMhcfAydNVWZnd2ZVVaAcGBsLf3x8//PAD7O3twRhDXFwcpk2bhpycHMyaNUsR6RNCCCGEEKKRqIgnRM28vb2xbds2ODg4wMjISCOWjiuz0A4KCsIvv/yCiRMnisdcXFzQrl07LFmyhIp4QgghhBBSq9FyekLUzNDQEHv37oWzs7O6U6kyCwsLLF26VKLQBoCwsDAsWbIE9+/f5x1bV1cXN27cgLW1tcR4Wloa2rdvj8LCQt6xCSGEEEII0XQCdSdASG3XsGFDWFpaqjsNmTx+/Bi9e/eWGu/duzceP34sV2xra2scPHhQavzAgQOwsbGRKzYhhBBCCCGajpbTE6JmS5YswdKlS7Fr1y7o6empO50qKSu0FyxYIDGuiEJ76dKlGD16NM6dOwd7e3twHIfz588jJiamwuKeEEIIIYSQ2oSW0xOiZvn5+XB1dUVcXBzMzc2ljoFLTExUU2aVO3LkCEaPHo3BgwdXWGiPGjVKrviJiYkIDAzE7du3wRhD27ZtMWfOHHTu3FlBr4AQQgghhBDNRDPxhKiZu7s7rly5gvHjx2tMY7svv/wSCQkJCAwMRFRUlLjQTkhIkKvQLioqwtSpU+Hv74+9e/cqMGNCCCGEEEJqBpqJJ0TN6tWrh5MnT6JPnz7qTqVKPiy0lbGX38DAAImJiRrXJ4AQQgghhBBVoMZ2hKiZiYkJ9PX11Z1Gleno6CAyMlJp8UeNGoWoqCilxSeEEEIIIUST0XJ6QtRs3bp1mDt3LkJCQmBubq7udKqkrNCePXu2wmNbW1tj+fLliI+PR5cuXVCvXj2J6zNmzFD4cxJCCCGEEKIpaDk9IWrWqFEj5Ofno7i4GHXr1pVqbPfixQs1ZVa5gIAArF27FoMGDVJ4oW1hYVHpNY7jkJ6ezjs2IYQQQgghmo6KeELULCws7KPX3dzcVJRJ1amq0C779aQJzf4IIYQQQghRBSriCSFyUUahvXPnTqxfvx5paWkAABsbG8ycOROenp4Kew5CCCGEEEI0ETW2I0QN8vLyJP77Y1/V1c6dO2FnZwddXV3o6urCzs4OO3bskDuuv78/vL29MXz4cBw6dAiHDh3C8OHDMWvWLPz4448KyJwQQgghhBDNRTPxhKiBlpYWHj9+jGbNmkEgEFQ4i80YA8dxEIlEasjw4/z9/bF+/Xp4eXmhV69eAIC///4bwcHB8Pb2xooVK3jHbtKkCYKCgjB27FiJ8fDwcHh5eSEnJ0eu3AkhhBBCCNFkVMQTogaxsbGwt7eHtrY2zp49+9Gl6P3791dhZlWjzEK7UaNGSEhIgI2NjcT4nTt30L17d+Tm5vKOTQghhBBCiKajIp4QIjNlFtpeXl7Q0dFBYGCgxLiPjw8KCgqwefNm3rEJIYQQQgjRdFTEE6Jm9vb26N+/PwYMGAB7e3up49qqI2UW2l5eXtizZw9MTEzQs2dPAMCFCxeQlZWFiRMnShzBV/75CSGEEEIIqemoiCdEzX7++WfExsYiPj4ehYWF6NKli7io79OnD+rXr6/uFKUos9B2cHCo0uM4jsPp06dlik0IIYQQQoimoyKekGpCJBLh0qVLOHv2LM6ePYvTp0+D4zi8e/dO3alJoUKbEEIIIYQQ9dBWdwKEkFJpaWm4evUqrl69imvXrkFfXx99+/ZVd1oVOnPmjLpTIIQQQgghpFaimXhC1Gz06NE4d+4cSkpK0K9fP/Tr1w/9+/dHhw4d1J0aIYQQQgghpJqhIp4QNRMIBGjSpAnc3d3h4OCAvn37Vst98IQQQgghhBD1oyKeEDXLzc3FuXPncPbsWcTGxuLmzZvo2LEjBgwYgAEDBmDo0KHqTpEQQgghhBBSTVART0g1c+/ePaxYsQJ79+5FSUkJRCKRulMihBBCCCGEVBPU2I4QNXvx4gViY2PFXelv3rwJQ0NDuLi4VLkLPCGEEEIIIaR2oJl4QtRMS0sLTZo0Qd++fcVL6O3s7NSdFiGEEEIIIaQaoiKeEDW7du0aLC0txc3sMjIyEBkZibZt28LR0VHN2RFCCCGEEEKqEyriCVEzR0dHuLq6Ytq0acjNzUXr1q2ho6ODnJwcBAYGYvr06epOkRBCCCGEEFJNCNSdACG1XWJiIvr27QsAOHz4MIyMjJCRkYE9e/Zg06ZNas6OEEIIIYQQUp1QEU+ImuXn56NBgwYAgFOnTsHV1RUCgQA9e/ZERkaGmrMjhBBCCCGEVCdUxBOiZtbW1oiKikJWVhZOnjwp3gefnZ0NfX19NWdHCCGEEEIIqU6oiCdEzRYtWgQfHx+Ym5ujR48e6NWrF4DSWfnOnTurOTtCCCGEEEJIdUKN7QipBp48eYLHjx+jY8eOEAhK760lJCRAX18frVu3VnN2hBBCCCGEkOqCinhCCCGEEEIIIURD0HJ6QgghhBBCCCFEQ1ARTwghhBBCCCGEaAgq4gkhhBBCCCGEEA1BRTwhhBBCCCGEEKIhqIgnhBBCCCGEEEI0BBXxhBBCCCGEEEKIhqAinhBCCCGEEEII0RD/D6ABPThBe1/WAAAAAElFTkSuQmCC",
      "text/plain": [
       "<Figure size 1200x1000 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "correlation_matrix = data.corr()\n",
    "\n",
    "# Plot a heatmap of the correlation matrix\n",
    "plt.figure(figsize=(12, 10))\n",
    "sns.heatmap(correlation_matrix, cmap='coolwarm')\n",
    "plt.title(\"Correlation Heatmap\")\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Correlation with the target variable:\n",
      "rent             1.000000\n",
      "bathroom         0.677390\n",
      "property_size    0.588315\n",
      "LIFT             0.490032\n",
      "PB               0.483128\n",
      "balconies        0.472221\n",
      "lift             0.461437\n",
      "POOL             0.453851\n",
      "GYM              0.448649\n",
      "total_floor      0.436968\n",
      "swimming_pool    0.434263\n",
      "gym              0.431120\n",
      "CLUB             0.427005\n",
      "SECURITY         0.412161\n",
      "FS               0.410886\n",
      "INTERCOM         0.396101\n",
      "CPA              0.339661\n",
      "VP               0.318468\n",
      "HK               0.307470\n",
      "floor            0.306242\n",
      "RWH              0.286969\n",
      "STP              0.274494\n",
      "AC               0.235029\n",
      "GP               0.224291\n",
      "SERVANT          0.204210\n",
      "longitude        0.163755\n",
      "PARK             0.141179\n",
      "negotiable       0.062429\n",
      "latitude         0.032829\n",
      "cup_board       -0.001245\n",
      "SC              -0.009572\n",
      "property_age    -0.010619\n",
      "INTERNET        -0.021140\n",
      "Name: rent, dtype: float64\n"
     ]
    }
   ],
   "source": [
    "# Extract correlations with the target variable\n",
    "target_correlations = correlation_matrix['rent'].sort_values(ascending=False)\n",
    "\n",
    "print(\"Correlation with the target variable:\")\n",
    "print(target_correlations)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Unnamed: 0</th>\n",
       "      <th>id</th>\n",
       "      <th>type</th>\n",
       "      <th>locality</th>\n",
       "      <th>activation_date</th>\n",
       "      <th>latitude</th>\n",
       "      <th>longitude</th>\n",
       "      <th>lease_type</th>\n",
       "      <th>gym</th>\n",
       "      <th>lift</th>\n",
       "      <th>...</th>\n",
       "      <th>SERVANT</th>\n",
       "      <th>SECURITY</th>\n",
       "      <th>SC</th>\n",
       "      <th>GP</th>\n",
       "      <th>PARK</th>\n",
       "      <th>RWH</th>\n",
       "      <th>STP</th>\n",
       "      <th>HK</th>\n",
       "      <th>PB</th>\n",
       "      <th>VP</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>7249</th>\n",
       "      <td>7249</td>\n",
       "      <td>ff80818151669a40015180250fa54e4d</td>\n",
       "      <td>BHK2</td>\n",
       "      <td>Doddanekundi</td>\n",
       "      <td>2018-02-16 09:57:00</td>\n",
       "      <td>12.971877</td>\n",
       "      <td>77.695300</td>\n",
       "      <td>FAMILY</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3118</th>\n",
       "      <td>3118</td>\n",
       "      <td>ff808181639be5140163a2019f417f28</td>\n",
       "      <td>BHK2</td>\n",
       "      <td>Doddanekkundi</td>\n",
       "      <td>2018-07-29 19:41:00</td>\n",
       "      <td>12.977272</td>\n",
       "      <td>77.679756</td>\n",
       "      <td>ANYONE</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>16200</th>\n",
       "      <td>16200</td>\n",
       "      <td>ff808181577fe2c60157850f49dc0e88</td>\n",
       "      <td>RK1</td>\n",
       "      <td>Koramangala</td>\n",
       "      <td>2017-11-21 15:15:00</td>\n",
       "      <td>12.928461</td>\n",
       "      <td>77.632793</td>\n",
       "      <td>ANYONE</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4306</th>\n",
       "      <td>4306</td>\n",
       "      <td>ff808181597a44b501597d9f1bac24c8</td>\n",
       "      <td>BHK2</td>\n",
       "      <td>Panathur</td>\n",
       "      <td>2018-06-22 19:05:00</td>\n",
       "      <td>12.936200</td>\n",
       "      <td>77.705575</td>\n",
       "      <td>ANYONE</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>17536</th>\n",
       "      <td>17536</td>\n",
       "      <td>ff8081815fa638b3015fa9b8c74e1e3f</td>\n",
       "      <td>BHK2</td>\n",
       "      <td>Kumaraswamy Layout</td>\n",
       "      <td>2017-11-11 13:09:00</td>\n",
       "      <td>12.905185</td>\n",
       "      <td>77.562918</td>\n",
       "      <td>FAMILY</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6994</th>\n",
       "      <td>6994</td>\n",
       "      <td>ff8081815e756939015e79a3529a650b</td>\n",
       "      <td>BHK2</td>\n",
       "      <td>JP Nagar 1st Phase</td>\n",
       "      <td>2017-09-13 12:17:00</td>\n",
       "      <td>12.907097</td>\n",
       "      <td>77.573176</td>\n",
       "      <td>ANYONE</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18738</th>\n",
       "      <td>18738</td>\n",
       "      <td>ff808181633a5aa701633b2e53803872</td>\n",
       "      <td>BHK2</td>\n",
       "      <td>Marathahalli</td>\n",
       "      <td>2018-08-05 10:24:00</td>\n",
       "      <td>12.955090</td>\n",
       "      <td>77.703055</td>\n",
       "      <td>FAMILY</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2539</th>\n",
       "      <td>2539</td>\n",
       "      <td>ff8081816035b0e50160369423b02bbd</td>\n",
       "      <td>BHK1</td>\n",
       "      <td>HSR Layout 5th Sector</td>\n",
       "      <td>2018-04-01 17:45:00</td>\n",
       "      <td>12.917139</td>\n",
       "      <td>77.629556</td>\n",
       "      <td>FAMILY</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19329</th>\n",
       "      <td>19329</td>\n",
       "      <td>ff8081815511306d0155162515f1438e</td>\n",
       "      <td>BHK2</td>\n",
       "      <td>Munnekollal</td>\n",
       "      <td>2017-06-09 16:01:00</td>\n",
       "      <td>12.944898</td>\n",
       "      <td>77.708082</td>\n",
       "      <td>ANYONE</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>20435</th>\n",
       "      <td>20435</td>\n",
       "      <td>ff8081815e7a0b30015e7b4995132c5f</td>\n",
       "      <td>BHK3</td>\n",
       "      <td>Banashankari</td>\n",
       "      <td>2017-09-13 19:24:00</td>\n",
       "      <td>12.938951</td>\n",
       "      <td>77.560433</td>\n",
       "      <td>FAMILY</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>10 rows × 44 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "       Unnamed: 0                                id  type  \\\n",
       "7249         7249  ff80818151669a40015180250fa54e4d  BHK2   \n",
       "3118         3118  ff808181639be5140163a2019f417f28  BHK2   \n",
       "16200       16200  ff808181577fe2c60157850f49dc0e88   RK1   \n",
       "4306         4306  ff808181597a44b501597d9f1bac24c8  BHK2   \n",
       "17536       17536  ff8081815fa638b3015fa9b8c74e1e3f  BHK2   \n",
       "6994         6994  ff8081815e756939015e79a3529a650b  BHK2   \n",
       "18738       18738  ff808181633a5aa701633b2e53803872  BHK2   \n",
       "2539         2539  ff8081816035b0e50160369423b02bbd  BHK1   \n",
       "19329       19329  ff8081815511306d0155162515f1438e  BHK2   \n",
       "20435       20435  ff8081815e7a0b30015e7b4995132c5f  BHK3   \n",
       "\n",
       "                    locality      activation_date   latitude  longitude  \\\n",
       "7249            Doddanekundi  2018-02-16 09:57:00  12.971877  77.695300   \n",
       "3118           Doddanekkundi  2018-07-29 19:41:00  12.977272  77.679756   \n",
       "16200            Koramangala  2017-11-21 15:15:00  12.928461  77.632793   \n",
       "4306                Panathur  2018-06-22 19:05:00  12.936200  77.705575   \n",
       "17536     Kumaraswamy Layout  2017-11-11 13:09:00  12.905185  77.562918   \n",
       "6994      JP Nagar 1st Phase  2017-09-13 12:17:00  12.907097  77.573176   \n",
       "18738           Marathahalli  2018-08-05 10:24:00  12.955090  77.703055   \n",
       "2539   HSR Layout 5th Sector  2018-04-01 17:45:00  12.917139  77.629556   \n",
       "19329            Munnekollal  2017-06-09 16:01:00  12.944898  77.708082   \n",
       "20435           Banashankari  2017-09-13 19:24:00  12.938951  77.560433   \n",
       "\n",
       "      lease_type  gym  lift  ...  SERVANT  SECURITY SC GP  PARK  RWH  STP HK  \\\n",
       "7249      FAMILY  1.0   1.0  ...        0         1  1  0     1    1    0  1   \n",
       "3118      ANYONE  0.0   0.0  ...        0         0  0  0     1    1    0  0   \n",
       "16200     ANYONE  0.0   0.0  ...        0         0  1  0     1    0    0  0   \n",
       "4306      ANYONE  1.0   1.0  ...        0         1  1  0     1    0    0  1   \n",
       "17536     FAMILY  0.0   0.0  ...        0         0  1  0     1    0    0  0   \n",
       "6994      ANYONE  0.0   0.0  ...        0         0  1  0     1    0    0  0   \n",
       "18738     FAMILY  1.0   1.0  ...        0         1  0  0     1    1    1  1   \n",
       "2539      FAMILY  0.0   0.0  ...        0         0  0  0     1    0    0  0   \n",
       "19329     ANYONE  0.0   0.0  ...        0         0  0  0     0    0    0  0   \n",
       "20435     FAMILY  0.0   0.0  ...        0         0  1  0     1    0    0  0   \n",
       "\n",
       "       PB  VP  \n",
       "7249    0   0  \n",
       "3118    0   0  \n",
       "16200   0   0  \n",
       "4306    1   0  \n",
       "17536   0   0  \n",
       "6994    0   0  \n",
       "18738   1   0  \n",
       "2539    1   0  \n",
       "19329   0   0  \n",
       "20435   0   0  \n",
       "\n",
       "[10 rows x 44 columns]"
      ]
     },
     "execution_count": 56,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data = pd.read_csv('no_commas_location.csv',index_col=False)\n",
    "data.sample(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 20555 entries, 0 to 20554\n",
      "Data columns (total 44 columns):\n",
      " #   Column           Non-Null Count  Dtype  \n",
      "---  ------           --------------  -----  \n",
      " 0   Unnamed: 0       20555 non-null  int64  \n",
      " 1   id               20555 non-null  object \n",
      " 2   type             20555 non-null  object \n",
      " 3   locality         20555 non-null  object \n",
      " 4   activation_date  20555 non-null  object \n",
      " 5   latitude         20555 non-null  float64\n",
      " 6   longitude        20555 non-null  float64\n",
      " 7   lease_type       20555 non-null  object \n",
      " 8   gym              20555 non-null  float64\n",
      " 9   lift             20555 non-null  float64\n",
      " 10  swimming_pool    20555 non-null  float64\n",
      " 11  negotiable       20555 non-null  float64\n",
      " 12  furnishing       20555 non-null  object \n",
      " 13  parking          20555 non-null  object \n",
      " 14  property_size    20555 non-null  float64\n",
      " 15  property_age     20555 non-null  float64\n",
      " 16  bathroom         20555 non-null  float64\n",
      " 17  facing           20555 non-null  object \n",
      " 18  cup_board        20555 non-null  float64\n",
      " 19  floor            20555 non-null  float64\n",
      " 20  total_floor      20555 non-null  float64\n",
      " 21  water_supply     20555 non-null  object \n",
      " 22  building_type    20555 non-null  object \n",
      " 23  balconies        20555 non-null  float64\n",
      " 24  rent             20555 non-null  float64\n",
      " 25  LIFT             20555 non-null  int64  \n",
      " 26  GYM              20555 non-null  int64  \n",
      " 27  INTERNET         20555 non-null  int64  \n",
      " 28  AC               20555 non-null  int64  \n",
      " 29  CLUB             20555 non-null  int64  \n",
      " 30  INTERCOM         20555 non-null  int64  \n",
      " 31  POOL             20555 non-null  int64  \n",
      " 32  CPA              20555 non-null  int64  \n",
      " 33  FS               20555 non-null  int64  \n",
      " 34  SERVANT          20555 non-null  int64  \n",
      " 35  SECURITY         20555 non-null  int64  \n",
      " 36  SC               20555 non-null  int64  \n",
      " 37  GP               20555 non-null  int64  \n",
      " 38  PARK             20555 non-null  int64  \n",
      " 39  RWH              20555 non-null  int64  \n",
      " 40  STP              20555 non-null  int64  \n",
      " 41  HK               20555 non-null  int64  \n",
      " 42  PB               20555 non-null  int64  \n",
      " 43  VP               20555 non-null  int64  \n",
      "dtypes: float64(14), int64(20), object(10)\n",
      "memory usage: 6.9+ MB\n"
     ]
    }
   ],
   "source": [
    "#drop when corr value < 0.1 with rent data set\n",
    "columns_to_drop=['negotiable','cup_board','SC','property_age','INTERNET']\n",
    "df=data.drop(columns=columns_to_drop)\n",
    "data.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['Unnamed: 0', 'id', 'type', 'locality', 'latitude', 'longitude',\n",
       "       'lease_type', 'gym', 'lift', 'swimming_pool', 'furnishing', 'parking',\n",
       "       'property_size', 'bathroom', 'facing', 'floor', 'total_floor',\n",
       "       'water_supply', 'building_type', 'balconies', 'rent', 'LIFT', 'GYM',\n",
       "       'AC', 'CLUB', 'INTERCOM', 'POOL', 'CPA', 'FS', 'SERVANT', 'SECURITY',\n",
       "       'GP', 'PARK', 'RWH', 'STP', 'HK', 'PB', 'VP', 'age_of_property'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 58,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# calculate Age and drop the date time\n",
    "current_date = datetime.today()\n",
    "df['activation_date']=pd.to_datetime(data['activation_date'])\n",
    "df['age_of_property'] = (current_date - df['activation_date']).dt.days // 365\n",
    "df.drop(columns=['activation_date'],inplace=True)\n",
    "df.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {},
   "outputs": [],
   "source": [
    "#drop high correlated value > 0.8\n",
    "df.drop(columns=['lift','gym','swimming_pool'],inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAA/QAAAOlCAYAAADD96wwAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/YYfK9AAAACXBIWXMAAA9hAAAPYQGoP6dpAAEAAElEQVR4nOzdeXxN1/7/8ffOdEISiTmphhgzUDUVoQhqpnQwtYaUKjVVY2q0Zm0IaqypRdxqi5a6impVUfNUVK80VKkOSdVcWhGxf3/45XydJiE4GU7yej4e6/Fw1l57rc/eOb2P+zlr7bUN0zRNAQAAAAAAh+KU3QEAAAAAAIB7R0IPAAAAAIADIqEHAAAAAMABkdADAAAAAOCASOgBAAAAAHBAJPQAAAAAADggEnoAAAAAABwQCT0AAAAAAA6IhB4AAAAAAAdEQg8AdvLdd9/phRdeUOnSpeXu7i5PT09Vq1ZN0dHROn/+fHaHZ2PLli0yDENbtmy553OPHj2qMWPG6NSpU6mOhYeHKyAg4IHjux+GYah///5pHvvkk0/u+3oz6u+//9aYMWMydYyscuLECVksFu3atcv6XclIkaQxY8bIMAydPXs2m6/ilsyIJywsTGFhYXdtd+rUKRmGoZiYGLuNnVHLli1TlSpV5O7uroceekiDBg3SlStXMnRuQkKC+vfvrzJlyihfvnwqVaqUevbsqdOnT9u0i4mJSfe7kJCQYG2XlJSksmXLavr06fa8RACAJJfsDgAAcoN3331Xffv2VWBgoIYOHaqQkBAlJSVp//79mjdvnnbt2qVPP/00u8O0i6NHj2rs2LEKCwtLlbyPHDlSr7zySvYEls3+/vtvjR07VpIylOzlZEOGDFGTJk0UGhqqy5cva9euXTbHn3rqKZUtW1ZTpkzJpghxJx988IG6dOmiF198UdOmTdOxY8c0fPhwHT16VF9++eUdz01MTFT9+vV14cIFjR07ViEhIYqLi9Po0aP1xRdfKDY2Vl5eXjbnLF68WEFBQTZ1hQsXtv7b1dVVo0aN0quvvqquXbvaHAMAPBgSegB4QLt27dLLL7+sJk2aaPXq1bJYLNZjTZo00eDBg7Vhwwa7jPX3338rf/78qeqTk5N148YNm7GzQ9myZbN1fDy42NhYrV692vqdLVCggGrXrm3TxmKxyMfHJ1X9gzJNU9euXVO+fPns2m9O988//+js2bPy9/d/4L6Sk5M1dOhQNW3aVO+++64kqWHDhvLy8tLzzz+vzz//XC1atEj3/G3btun48eN677331LNnT0m3fqAqUKCAnnvuOX311Vd66qmnbM6pVKmSatSocce4OnfurIiICM2fP18jRox4wKsEAKRgyT0APKC33npLhmFowYIFaSbUbm5uevLJJ62fb968qejoaAUFBclisahYsWLq1q2bfv31V5vzwsLCVKlSJX3zzTeqU6eO8ufPrx49eliX8UZHR2vChAkqXbq0LBaLNm/eLEnav3+/nnzySRUqVEju7u6qWrWqVqxYcdfr2L9/vzp16qSAgADly5dPAQEB6ty5s37++Wdrm5iYGLVv317SrSQhZXltypLitJbcX7t2TZGRkSpdurTc3NxUokQJ9evXTxcvXrRpFxAQoNatW2vDhg2qVq2a8uXLp6CgIC1atOiusd+vjNyrP//8U3379lVISIg8PT1VrFgxNWrUSNu2bbO2OXXqlIoWLSpJGjt2rPW+hIeHS/q/Zd/fffed2rdvL29vbxUqVEgRERG6ceOG4uLi1Lx5c3l5eSkgIEDR0dE2MVy7dk2DBw9WlSpVrOeGhobqv//9b6prSnn0YP78+apQoYIsFotCQkK0bNmyDN2TuXPnytfXV02aNLmXW5nKH3/8oc6dO8vb21vFixdXjx49dOnSpTRjnTdvnoKDg2WxWLRkyRJJ0vHjx/Xcc8+pWLFislgsCg4O1jvvvGNz/s2bNzVhwgQFBgYqX7588vHxUeXKlTVjxoz7iiej39W0/P777+rQoYO8vLzk7e2tjh072iw7v9u9KlWqlOrXr6+5c+c+0OMBu3fvVnx8vF544QWb+vbt28vT0/OuK4VcXV0lSd7e3jb1Pj4+kiR3d/f7isvNzU0dO3bUggULZJrmffUBAEiNGXoAeADJycn6+uuvVb169QzPrr388stasGCB+vfvr9atW+vUqVMaOXKktmzZom+//VZFihSxto2Pj1eXLl00bNgwvfXWW3Jy+r/fYWfOnKkKFSpoypQpKlCggMqXL6/NmzerefPmqlWrlubNmydvb28tW7ZMHTt21N9//21NMNNy6tQpBQYGqlOnTipUqJDi4+M1d+5cPfbYYzp69KiKFCmiVq1a6a233tKIESP0zjvvqFq1apLSn5k3TVPt2rXTpk2bFBkZqXr16um7777T6NGjtWvXLu3atcvmR5DDhw9r8ODBeu2111S8eHHrLGG5cuVUv379u95b0zR148aNVPU3b95MVZfRe5Wy/8Ho0aPl6+urK1eu6NNPP1VYWJg2bdqksLAw+fn5acOGDWrevLl69uypF198UZKsSX6KDh06qEuXLurdu7c2btyo6OhoJSUl6auvvlLfvn01ZMgQffjhhxo+fLjKlSunp59+WtKtZdDnz5/XkCFDVKJECV2/fl1fffWVnn76aS1evFjdunWzGWfNmjXavHmzxo0bJw8PD82ZM0edO3eWi4uLnn322Tvew3Xr1ql+/fo237X78cwzz6hjx47q2bOnjhw5osjISElK9QPN6tWrtW3bNo0aNUq+vr4qVqyYjh49qjp16qhkyZKaOnWqfH199cUXX2jgwIE6e/asRo8eLUmKjo7WmDFj9MYbb6h+/fpKSkrSDz/8kGYCfrd47vW7ert//vlHTzzxhH7//XdFRUWpQoUKWrdunTp27Jihe+Xv769PP/1Uy5Yt09ChQzVw4EA1adJEnTt3Vrt27VItcb+T77//XpJUuXJlm3pXV1cFBQVZj6enbt26ql69usaMGaNSpUopODhYx44d04gRI1StWjU98cQTqc5p3bq1/vzzT3l7eyssLEzjxo1TpUqVUrULCwvT3Llz9f333+uRRx7J8DUBAO7ABADct4SEBFOS2alTpwy1j42NNSWZffv2tanfs2ePKckcMWKEta5BgwamJHPTpk02bU+ePGlKMsuWLWtev37d5lhQUJBZtWpVMykpyaa+devWpp+fn5mcnGyapmlu3rzZlGRu3rw53Vhv3LhhXrlyxfTw8DBnzJhhrf/444/TPbd79+5mqVKlrJ83bNhgSjKjo6Nt2i1fvtyUZC5YsMBaV6pUKdPd3d38+eefrXX//POPWahQIbN3797pxplC0l3L7TFn9F6ldV+SkpLMxo0bm0899ZS1/s8//zQlmaNHj051zujRo01J5tSpU23qq1SpYkoyV61aZa1LSkoyixYtaj799NPpXmtKDD179jSrVq2a6j7ky5fPTEhIsGkfFBRklitXLt0+TdM0//jjD1OSOXHixDu2K1WqlNmqVas0j6Vc67//5n379jXd3d3Nmzdv2sTq7e1tnj9/3qZts2bNzIcffti8dOmSTX3//v1Nd3d3a/vWrVubVapUuWOsGY3nXr6rDRo0MBs0aGD9PHfuXFOS+d///tfm3F69epmSzMWLF98xxttdvXrVXL58ufnUU0+Z7u7uZr58+cz27dubq1atMq9du3bX8998801TkhkfH5/qWNOmTc0KFSrctY/Lly+bbdq0sflvJywszDx37pxNu88//9x8/fXXzc8++8zcunWrOXv2bPPhhx82PTw8zEOHDqXq9/jx46Ykc+7cuXeNAQCQMSy5B4AslLIs/t8z5TVr1lRwcLA2bdpkU1+wYEE1atQozb6efPJJ6/JYSfrxxx/1ww8/6Pnnn5ck3bhxw1patmyp+Ph4xcXFpRvblStXrDPDLi4ucnFxkaenp65evarY2Nj7uVx9/fXXklJfb/v27eXh4ZHqeqtUqaKSJUtaP7u7u6tChQo2y/7vpEOHDtq3b1+qMmnSJJt293qv5s2bp2rVqsnd3V0uLi5ydXXVpk2b7vm+tG7d2uZzcHCwDMOweabZxcVF5cqVS3XNH3/8serWrStPT09rDAsXLkwzhsaNG6t48eLWz87OzurYsaN+/PHHVI923O7333+XJBUrVuyeristtz9mIt2aMb527ZrOnDljU9+oUSMVLFjQ+vnatWvatGmTnnrqKeXPnz/V3+batWvavXu3pFv/3Rw+fFh9+/bVF198ocuXL993PPf6Xb3d5s2b5eXllWqM5557Lt1z0pM/f3516NBBq1at0h9//KH58+fr6tWr6tChg4oXL64dO3ZkqJ+Utw5ktD5FUlKSOnbsqEOHDundd9/VN998oyVLlui3335TkyZNbB5TaN68uSZMmKDWrVurfv366tevn7Zt2ybDMDRq1KhUfad8r3777bcMXQMA4O5Ycg8AD6BIkSLKnz+/Tp48maH2586dkyT5+fmlOvbQQw+lSuLSapfesT/++EPSrR3KhwwZkuY5d3o297nnntOmTZs0cuRIPfbYYypQoIAMw1DLli31zz//pHvenZw7d04uLi6plp4bhiFfX1/r/UiR1u7XFoslw+MXLVo0zc25/v2KvXu5V2+//bYGDx6sPn36aPz48SpSpIicnZ01cuTIe07oCxUqZPPZzc1N+fPnT/Vcspubm01yumrVKnXo0EHt27fX0KFD5evrKxcXF82dOzfNPQZ8fX3TrTt37pwefvjhNONLuc/3+5z07f79t0xZrv7vv+W/v8fnzp3TjRs3NGvWLM2aNSvNvlP+NpGRkfLw8NDSpUs1b948OTs7q379+po0aVKq78Hd4rnX7+q/Y779B5QUaf0d7sXVq1d18eJFXbp0ScnJyfLy8pKbm9sdz0m5zrRiOn/+fKrv4L8tXLhQn3/+ufbt22e9h/Xq1dPjjz9uffVcyiMPaQkICNDjjz9u/dHldinfq/v93xMAQGok9ADwAJydndW4cWN9/vnn+vXXX9NNlFKk/J/t+Pj4VG1///13m+fnpTvPpv37WMq5kZGR1mev/y0wMDDN+kuXLmnt2rUaPXq0XnvtNWt9yrPb96tw4cK6ceOG/vzzT5tEyTRNJSQk6LHHHrvvvh/EvdyrpUuXWp/9vd1ff/2VuUHeZunSpSpdurSWL19u83dPTExMs31am7Gl1N3plWEp9+VB/ub36t/f44IFC8rZ2Vldu3ZVv3790jyndOnSkm6tZoiIiFBERIQuXryor776SiNGjFCzZs30yy+/pPlGiPQ8yHe1cOHC2rt3b6r6jG6Kd7uzZ89q5cqVWrZsmb755hsVLFhQzzzzjN58803Vr1//rjPsKc+mHzlyRCEhIdb6Gzdu6IcfflDnzp3veP6hQ4fk7Oxs3R8jRZkyZVS4cOG7PoMv3bpnae3BkPK9+vf/zgEA7h9L7gHgAUVGRso0TfXq1UvXr19PdTwpKUmfffaZJFmXzy9dutSmzb59+xQbG6vGjRvfdxyBgYEqX768Dh8+rBo1aqRZ0ttcyzAMmaaZatOv9957T8nJyTZ16c20piXlev59vStXrtTVq1cf6HofxL3cK8MwUt2X7777LtW72e/lvtwrwzDk5uZmk8wlJCSkucu9JG3atMm6CkG6tXnj8uXLVbZs2Tv+6FSqVCnly5dPJ06csF/w9yh//vxq2LChDh48qMqVK6f5t0nrRwkfHx89++yz6tevn86fP59qVcbdPMh3tWHDhvrrr7+0Zs0am/oPP/wwQ2Nfv35dixYtUrNmzeTn56fBgwfLz89P//3vfxUfH6/58+erQYMGd03mJalWrVry8/OzvnkixSeffKIrV66k+wNWioceekjJycnat2+fTf2xY8fuuLojxcmTJ7Vjx440X2n4008/SZLNDw0AgAfDDD0APKDQ0FDNnTtXffv2VfXq1fXyyy+rYsWKSkpK0sGDB7VgwQJVqlRJbdq0UWBgoF566SXNmjVLTk5OatGihXWXe39/f7366qsPFMv8+fPVokULNWvWTOHh4SpRooTOnz+v2NhYffvtt/r444/TPK9AgQKqX7++Jk+erCJFiiggIEBbt27VwoULra+rSpGye/WCBQvk5eUld3d3lS5dOs0kq0mTJmrWrJmGDx+uy5cvq27dutadw6tWraquXbs+0PU+iIzeq9atW2v8+PEaPXq0GjRooLi4OI0bN06lS5e22VHfy8tLpUqV0n//+181btxYhQoVst7LB9W6dWutWrVKffv21bPPPqtffvlF48ePl5+fn44fP56qfZEiRdSoUSONHDnSusv9Dz/8cNdX17m5uSk0NDTN5dJZacaMGXr88cdVr149vfzyywoICNBff/2lH3/8UZ999pn1efc2bdpY34FetGhR/fzzz5o+fbpKlSql8uXL39OYD/Jd7datm6ZNm6Zu3brpzTffVPny5bV+/Xp98cUXGRr7999/V58+fdSsWTP95z//Udu2be9pdcHtnJ2dFR0dra5du6p3797q3Lmzjh8/rmHDhqlJkyZq3ry5te3WrVvVuHFjjRo1yvrM+wsvvKBp06bpmWee0RtvvKHAwED99NNPeuutt+Th4aE+ffpYz3/iiSdUv359Va5cWQUKFNCRI0cUHR0twzA0fvz4VLHt3r3b+lgEAMBOsnVLPgDIRQ4dOmR2797dLFmypOnm5mZ6eHiYVatWNUeNGmWeOXPG2i45OdmcNGmSWaFCBdPV1dUsUqSI2aVLF/OXX36x6a9BgwZmxYoVU42Tssv95MmT04zj8OHDZocOHcxixYqZrq6upq+vr9moUSNz3rx51jZp7XL/66+/ms8884xZsGBB08vLy2zevLn5/fffm6VKlTK7d+9uM8b06dPN0qVLm87Ozja7eP97l3vTvLVT/fDhw81SpUqZrq6upp+fn/nyyy+bFy5csGmX3s7p/95RPD2SzH79+qV5LL2d+TNyrxITE80hQ4aYJUqUMN3d3c1q1aqZq1evTvNav/rqK7Nq1aqmxWIxJVnvW8pO63/++adN++7du5seHh5pXvO///YTJ040AwICTIvFYgYHB5vvvvuutd+07sOcOXPMsmXLmq6urmZQUJD5wQcf3On2WS1cuNB0dnY2f//993TbZGSX+39f6+LFi01J5smTJ1PFmpaTJ0+aPXr0MEuUKGG6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ixdr7ty5+t///qdXX31VXbp00datWzN+YwAAAADADpycjRxbcos8ueT++PHjWrNmjXbs2KE6depIkj744AP5+/tr9erVat++vSQpKSlJ8+bNU9myZSVJ/fv317hx46z9zJo1S5GRkXrqqackSbNnz9b69evTHbdQoUJydnaWl5eXfH197ynm6dOnKzIyUs8884wkad68efriiy+sx69evaq3335bX3/9tUJDQyVJZcqU0fbt2zV//nw1aNAgzX4TExOVmJhoU2exWGSxWO4pPgAAAABA1sqTM/SxsbFycXFRrVq1rHWFCxdWYGCgYmNjrXX58+e3JvOS5OfnpzNnzkiSLl26pD/++EM1a9a0Hnd2dlb16tXtHu+lS5cUHx9vTdQlycXFRTVq1LB+Pnr0qK5du6YmTZrI09PTWv7zn//oxIkT6fYdFRUlb29vmxIVFWX3awAAAAAA2FeenKH/97Pnt9enPNcuyWZ3ekkyDCPVube3v1Pfd+Lk5JTqvNuX/mfEzZs3JUnr1q1TiRIlbI7dabY9MjJSERERGW4PAAAAABnBLveZL0/O0IeEhOjGjRvas2ePte7cuXM6duyYgoODM9SHt7e3ihcvrr1791rrkpOTdfDgwTue5+bmpuTkZJu6okWLKiEhwSapP3TokM1Yfn5+2r17t7Xuxo0bOnDggM01WSwWnT59WuXKlbMp/v7+6cZjsVhUoEABm0JCDwAAAAA5X56coS9fvrzatm2rXr16af78+fLy8tJrr72mEiVKqG3bthnuZ8CAAYqKilK5cuUUFBSkWbNm6cKFC6lm7W8XEBCgb775Rp06dZLFYlGRIkUUFhamP//8U9HR0Xr22We1YcMGff755ypQoID1vFdeeUUTJ05U+fLlFRwcrLffflsXL160Hvfy8tKQIUP06quv6ubNm3r88cd1+fJl7dy5U56enurevft93SsAAAAAQM6UJ2foJWnx4sWqXr26WrdurdDQUJmmqfXr16daZn8nw4cPV+fOndWtWzeFhobK09NTzZo1k7u7e7rnjBs3TqdOnVLZsmVVtGhRSVJwcLDmzJmjd955R48++qj27t1rs5u+JA0ePFjdunVTeHi4QkND5eXlZd2ML8X48eM1atQoRUVFKTg4WM2aNdNnn32m0qVL38OdAQAAAIAHZzg55diSWxjm/Tz0jTTdvHlTwcHB6tChg8aPH5/d4SAN61wDs3S8VklxWToeAAAAkFPEPtMku0NIV/DKjdkdgl3kySX39vLzzz/ryy+/VIMGDZSYmKjZs2fr5MmTeu6557I7NAAAAABALkdC/wCcnJwUExOjIUOGyDRNVapUSV999VWGN9YDAAAAgNyKXe4zHwn9A/D399eOHTuyOwwAAAAAQB6Ue3YDAAAAAAAgD2GGHgAAAABgdyy5z3zM0AMAAAAA4IBI6AEAAAAAcEAsuQcAAAAA2B1L7jMfM/QAAAAAADggZuiRp7RKisvS8da5BmbZWFl9bQAAAACyFwk9AAAAAMDuDCcWhGc27jAAAAAAAA6IhB4AAAAAAAfEknsAAAAAgN05ObPLfWZjhh4AAAAAAAdEQg8AAAAAgAMioc/hAgICNH369OwOAwAAAADuieFk5NiSW/AM/T0KCwtTlSpVsizJ3rdvnzw8PLJkLAAAAACA43CoGfrr169n29hJSUnZMm7RokWVP3/+bBkbAAAAAJBzZWtCHxYWpv79+6t///7y8fFR4cKF9cYbb8g0TUm3lptPmDBB4eHh8vb2Vq9evSRJK1euVMWKFWWxWBQQEKCpU6fa9BsQEKDx48frueeek6enpx566CHNmjXLps2lS5f00ksvqVixYipQoIAaNWqkw4cPW4+PGTNGVapU0aJFi1SmTBlZLBZ1795dW7du1YwZM2QYhgzD0MmTJ1WuXDlNmTLFpv/vv/9eTk5OOnHixF3vw5gxY1SyZElZLBY99NBDGjhwoM21pKwGiImJsY57exkzZoy1/eLFixUcHCx3d3cFBQVpzpw5d/9DAAAAAICdGU5OObbkFtl+JUuWLJGLi4v27NmjmTNnatq0aXrvvfesxydPnqxKlSrpwIEDGjlypA4cOKAOHTqoU6dOOnLkiMaMGaORI0cqJibGpt/JkyercuXK+vbbbxUZGalXX31VGzdulCSZpqlWrVopISFB69ev14EDB1StWjU1btxY58+ft/bx448/asWKFVq5cqUOHTqkmTNnKjQ0VL169VJ8fLzi4+NVsmRJ9ejRQ4sXL7YZf9GiRapXr57Kli17x+v/5JNPNG3aNM2fP1/Hjx/X6tWr9cgjj6TZtmPHjtZx4+Pj9dFHH8nFxUV169aVJL377rt6/fXX9eabbyo2NlZvvfWWRo4cqSVLlmT47wEAAAAAcAzZ/gy9v7+/pk2bJsMwFBgYqCNHjmjatGnW2fhGjRppyJAh1vbPP/+8GjdurJEjR0qSKlSooKNHj2ry5MkKDw+3tqtbt65ee+01a5sdO3Zo2rRpatKkiTZv3qwjR47ozJkzslgskqQpU6Zo9erV+uSTT/TSSy9JurXE//3331fRokWt/bq5uSl//vzy9fW11r3wwgsaNWqU9u7dq5o1ayopKUlLly7V5MmT73r9p0+flq+vr5544gm5urqqZMmSqlmzZppt8+XLp3z58kmSTpw4of79++utt95SkyZNJEnjx4/X1KlT9fTTT0uSSpcuraNHj2r+/Pnq3r37XWMBAAAAADiObJ+hr127tgzj/3YZDA0N1fHjx5WcnCxJqlGjhk372NhY64x0irp169qck9LP7UJDQxUbGytJOnDggK5cuaLChQvL09PTWk6ePGmzRL5UqVI2yXx6/Pz81KpVKy1atEiStHbtWl27dk3t27e/67nt27fXP//8ozJlyqhXr1769NNPdePGjTuec+nSJbVu3VotWrTQ0KFDJUl//vmnfvnlF/Xs2dPmmiZMmHDHZf+JiYm6fPmyTUlMTLxr3AAAAABwJ9m9kz273OcA/97h3TRNmx8AUuoyIuW8mzdvys/PT1u2bEnVxsfHJ92x7+TFF19U165dNW3aNC1evFgdO3bM0GZ2/v7+iouL08aNG/XVV1+pb9++mjx5srZu3SpXV9dU7ZOTk9WxY0cVKFBA7777rrX+5s2bkm4tu69Vq5bNOc7OzumOHxUVpbFjx9rUjR492ua5fAAAAABAzpPtCf3u3btTfS5fvny6SWhISIi2b99uU7dz505VqFDB5py0+g0KCpIkVatWTQkJCXJxcVFAQMA9xevm5mazEiBFy5Yt5eHhoblz5+rzzz/XN998k+E+8+XLpyeffFJPPvmk+vXrp6CgIB05ckTVqlVL1fbVV1/VkSNHtG/fPrm7u1vrixcvrhIlSuinn37S888/n+GxIyMjFRERYVOX8hgCAAAAACDnyvaE/pdfflFERIR69+6tb7/9VrNmzUq1a/3tBg8erMcee0zjx49Xx44dtWvXLs2ePTvVbu47duxQdHS02rVrp40bN+rjjz/WunXrJElPPPGEQkND1a5dO02aNEmBgYH6/ffftX79erVr1y7VMv/bBQQEaM+ePTp16pQ8PT1VqFAh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lrWucOHCCgwMVGxsrLVN3bp1bc6rW7eujh8/ruTkZGtdjRo17jpeYmKiLl++bFMSExPtdDUAAAAA8iwnI+eWXIKEPocxTTPdesMwUv37Tud5eHjcdbyoqCh5e3vblKioqPuIHAAAAAByrzlz5qh06dJyd3dX9erVtW3btju2f+eddxQcHKx8+fIpMDBQ//nPf2yOx8TEyDCMVOXatWsZjokl9zlMSEiIbty4oT179liX3J87d07Hjh1TcHCwtc327dttztu5c6cqVKggZ2fnexovMjJSERERNnUWi+UBrgAAAAAAcpfly5dr0KBBmjNnjurWrav58+erRYsWOnr0qEqWLJmq/dy5cxUZGal3331Xjz32mPbu3atevXqpYMGCatOmjbVdgQIFFBcXZ3Ouu7t7huMioc9hypcvr7Zt26pXr16aP3++vLy89Nprr6lEiRJq27atJGnw4MF67LHHNH78eHXs2FG7du3S7NmzNWfOnHsez2KxkMADAAAAsDvDKfcsCH/77bfVs2dPvfjii5Kk6dOn64svvtDcuXPTXOH8/vvvq3fv3urYsaMkqUyZMtq9e7cmTZpkk9AbhpHm3moZlXvucC6yePFiVa9eXa1bt1ZoaKhM09T69evl6uoqSapWrZpWrFihZcuWqVKlSho1apTGjRtnsyEeAAAAACBt97KX2PXr13XgwAE1bdrUpr5p06bauXNnuv3/e6Y9X7582rt3r/XtZZJ05coVlSpVSg8//LBat26tgwcP3tN1GGZ6D20DwB2scw3MsrFaJcXdvREAAABylIuT+md3COma/k8RjR071qZu9OjRGjNmTKq2v//+u0qUKGHzJjJJeuutt7RkyZJUS+YlacSIEVq8eLHWrl2ratWq6cCBA2rVqpXOnDmj33//XX5+ftq9e7d+/PFHPfLII7p8+bJmzJih9evX6/DhwypfvnyGroMl9wAAAAAAuzNy8G7y97OXWFobk/+7LsXIkSOVkJCg2rVryzRNFS9eXOHh4YqOjrbue1a7dm3Vrl3bek7dunVVrVo1zZo1SzNnzszQdbDkHgAAAACQp1gsFhUoUMCmpJfQFylSRM7OzkpISLCpP3PmjIoXL57mOfny5dOiRYv0999/69SpUzp9+rQCAgLk5eWlIkWKpHmOk5OTHnvsMR0/fjzD10FCDwAAAABAOtzc3FS9enVt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xDTbXr9+XQcOHFDTpk1t6ps2baqdO3em27+7u7tNXb58+bR3714lJSVJujVD/+8+mzVrlm6faSGhdyA7d+6Us7OzmjdvnurY9evXFR0drUcffVT58+dXkSJFVLduXS1evNj6hQEAAACALGM45dgSFRUlb29vm5LWTLsknT17VsnJySpevLhNffHixZWQkJDmOc2aNdN7772nAwcOyDRN7d+/X4sWLVJSUpLOnj0rSUpISLinPtPCa+scyKJFizRgwAC99957On36tEqWLCnpVjLfrFkzHT58WOPHj1fdunVVoEAB7d69W1OmTFHVqlVVpUqV7A0eAAAAAHKIyMhIRURE2NRZLJY7nmMYtq/hM00zVV2KkSNHKiEhQbVr15ZpmipevLjCw8MVHR0tZ2fn++ozLST0DuLq1atasWKF9u3bp4SEBMXExGjUqFGSpOnTp+ubb77R/v37VbVqVes5ZcqUUfv27XX9+vXsChsAAAAAchyLxXLXBD5FkSJF5OzsnGrm/MyZM6lm2FPky5dPixYt0vz58/XHH3/Iz89PCxYskJeXl4oUKSJJ8vX1vac+08KSewexfPlyBQYGKjAwUF26dNHixYuVsp/hBx98oCeeeMImmU/h6uoqDw+PrA4XAAAAQB5nGkaOLffCzc1N1atX18aNG23qN27cqDp16tzxXFdXVz388MNydnbWsmXL1Lp1azk53UrDQ0NDU/X55Zdf3rXP2zFD7yAWLlyoLl26SLq18+GVK1e0adMmPfHEEzp+/LjCwsKyN0AAAAAAyKUiIiLUtWtX1ahRQ6GhoVqwYIFOnz6tPn36SLq1hP+3336zvmv+2LFj2rt3r2rVqqULFy7o7bff1vfff68lS5ZY+3zllVdUv359TZo0SW3bttV///tfffXVV9Zd8DOChN4BxMXFae/evVq1apUkycXFRR07dtSiRYv0xBNP3PNzFrdLTExMtZvjvSw/AQAAAIDcrmPHjjp37pzGjRun+Ph4VapUSevXr1epUqUkSfHx8TbvpE9OTtbUqVMVFxcnV1dXNWzYUDt37lRAQIC1TZ06dbRs2TK98cYbGjlypMqWLavly5erVq1aGY6L99A7gGHDhmny5Mk2myeYpilXV1fFx8crLCxMvr6++uKLL+657zFjxmjs2LE2daNHj9aYMWMeNGwAyFK8hx4AgJzl/HfbsjuEdBWqXC+7Q7ALEvoc7saNG3r44Yc1bNiwVO8ofOaZZzRgwABdvXpVI0aMSLUpXsr5iYmJ6T5Hzww9gNyChB4AgJyFhD7zseQ+h1u7dq0uXLignj17ytvb2+bYs88+q4ULF2r37t1at26dGjdurPHjx+vxxx+Xl5eX9u/fr0mTJmnhwoXpvraO5B0AAAAAHBMz9DlcmzZtdPPmTa1bty7VsW+//VbVq1fXgQMHVLFiRU2bNk0ffvihjh8/rvz58ys4OFi9evXS888/LxcXfrsBkLsxQw8AQM5y/kjGN3fLaoUeeTy7Q7ALEnoAQK5AQg8AQM5CQp/5eA89AAAAAAAOiHXYAAAAAAC7Mw3mjzMbdxgAAAAAAAdEQg8AAAAAgANiyT0AAAAAwO5MGdkdQq7HDD0AAAAAAA6IhB4AAAAAAAfEknsAAAAAgN2xy33m4w4DAAAAAOCAmKEHAOQKrZLisnS8da6BWTZWVl8bAABwDCT0AAAAAAD7M9jlPrOx5B4AAAAAAAdEQg8AAAAAgANiyT0AAAAAwO5M5o8zHXcYAAAAAAAHREIPAAAAAIADYsk9AAAAAMDuTHa5z3TM0AMAAAAA4IBI6LNAQkKCBgwYoDJlyshiscjf319t2rTRpk2bJEkBAQGaPn16mucahqHVq1enqh80aJDCwsKsn8PDw2UYhrUULlxYzZs313fffZcJVwQAAAAAyG4k9Jns1KlTql69ur7++mtFR0fryJEj2rBhgxo2bKh+/frZdazmzZsrPj5e8fHx2rRpk1xcXNS6dWu7jgEAAAAAGWEaTjm25BY8Q5/J+vbtK8MwtHfvXnl4eFjrK1asqB49eth1LIvFIl9fX0mSr6+vhg8frvr16+vPP/9U0aJF7ToWAAAAACB75Z6fJnKg8+fPa8OGDerXr59NMp/Cx8cn08a+cuWKPvjgA5UrV06FCxfOtHEAAAAAANmDGfpM9OOPP8o0TQUFBWXJeGvXrpWnp6ck6erVq/Lz89PatWvl5MTvNgAAAACylil2uc9sZHqZyDRNSbc2tssKDRs21KFDh3To0CHt2bNHTZs2VYsWLfTzzz+ne05iYqIuX75sUxITE7MkXgAAAADA/SOhz0Tly5eXYRiKjY297z68vLx06dKlVPUXL16Ut7e3TZ2Hh4fKlSuncuXKqWbNmlq4cKGuXr2qd999N93+o6Ki5O3tbVOioqLuO14AAAAAQNYgoc9EhQoVUrNmzfTOO+/o6tWrqY5fvHjxrn0EBQVp3759NnWmaerAgQMKDAy847mGYcjJyUn//PNPum0iIyN16dIlmxIZGXnXuAAAAADgTrJ7J3t2uccDmzNnjurUqaOaNWtq3Lhxqly5sm7cuKGNGzdq7ty51tn73377TYcOHbI5t2TJkhoyZIi6d++uoKAgNW3aVP/8848WLFigEydOpHrtXWJiohISEiRJFy5c0OzZs3XlyhW1adMm3fgsFossFot9LxoAAAAAkOlI6DNZ6dKl9e233+rNN9/U4MGDFR8fr6JFi6p69eqaO3eutd2UKVM0ZcoUm3MXL16s8PBwmaapKVOm6PXXX5e7u7uqVq2qbdu2qVSpUjbtN2zYID8/P0m3luoHBQXp448/VlhYWKZfJwAAAAAgaxlmys5tAAAgw9a53vmxJ3tqlRSXZWMBAGAvvx07kt0hpKtEhUeyOwS7yD0PDwAAAAAAkIeQ0AMAAAAA4IB4hh4AAAAAYHemjOwOIddjhh4AAAAAAAdEQg8AAAAAgANiyT0AAAAAwO5Mg/njzMYdBgAAAADAAZHQAwAAAADggFhyDwAAAACwO3a5z3wk9AAA3IdWSXFZNtY618AsG0vK2msDAAD3jyX3AAAAAAA4IGboAQAAAAB2xy73mY87DAAAAACAAyKhBwAAAADAAbHkHgAAAABgd+xyn/mYoQcAAAAAwAGR0AMAAAAA4IByVUIfHh6udu3aWf9tGIYmTpxo02b16tUyDMOmzZ3Kndo1b97c2m9AQIC1Pl++fAoKCtLkyZNlmqbN+AcPHlT79u1VvHhxubu7q0KFCurVq5eOHTtm027JkiWqWbOmPDw85OXlpfr162vt2rU2bbZs2SLDMFSwYEFdu3bN5tjevXttrgEAAAAAspJpOOXYklvknitJg7u7uyZNmqQLFy6keXzGjBmKj4+3FklavHhxqjpJat68uU19fHy8PvroI5v+xo0bp/j4eMXGxmrIkCEaMWKEFixYYD2+du1a1a5dW4mJifrggw8UGxur999/X97e3ho5cqS13ZAhQ9S7d2916NBBhw8f1t69e1WvXj21bdtWs2fPTnUdXl5e+vTTT23qFi1apJIlS977TQMAAAAAOIRcvSneE088oR9//FFRUVGKjo5Oddzb21ve3t42dT4+PvL19U3V1mKxpFl/Oy8vL2ubF198UXPnztWXX36p3r176++//9YLL7ygli1b2iTfpUuXVq1atXTx4kVJ0u7duzV16lTNnDlTAwYMsLZ78803de3aNUVERKht27by9/e3HuvevbsWLVqkzp07S5L++ecfLVu2TAMHDtT48ePvcpcAAAAAAI4oV8/QOzs766233tKsWbP066+/Ztm4pmlqy5Ytio2NlaurqyTpiy++0NmzZzVs2LA0z/Hx8ZEkffTRR/L09FTv3r1TtRk8eLCSkpK0cuVKm/quXbtq27ZtOn36tCRp5cqVCggIULVq1ex4VQAAAACQcaaMHFtyi1yd0EvSU089pSpVqmj06NEP1M/atWvl6elpU/49+z18+HB5enrKYrGoYcOGMk1TAwcOlCQdP35ckhQUFHTHcY4dO6ayZcvKzc0t1bGHHnpI3t7eqZ63L1asmFq0aKGYmBhJt5bb9+jR434vFQAAAADgAHL1kvsUkyZNUqNGjTR48OD77qNhw4aaO3euTV2hQoVsPg8dOlTh4eH6888/9frrr6tRo0aqU6eOJKXaHO9+maaZ5kZ3PXr00CuvvKIuXbpo165d+vjjj7Vt27a79peYmKjExESbOovFIovFYpd4AQAAAACZI9fP0EtS/fr11axZM40YMeK++/Dw8FC5cuVsyr8T+iJFiqhcuXIKDQ3VypUrNW3aNH311VeSpAoVKkiSfvjhhzuOU6FCBZ04cULXr19Pdez333/X5cuXVb58+VTHWrZsqWvXrqlnz55q06aNChcunKHrioqKsu4lkFKioqIydC4AAAAApMc0jBxbcos8kdBL0sSJE/XZZ59p586dWTJewYIFNWDAAA0ZMkSmaapp06YqUqRImpvzSbJuitepUydduXJF8+fPT9VmypQpcnV11TPPPJPqmLOzs7p27aotW7bc03L7yMhIXbp0yaZERkZm+HwAAAAAQPbIE0vuJemRRx7R888/r1mzZt3X+YmJiUpISLCpc3FxUZEiRdI9p1+/fpo0aZJWrlypZ599Vu+9957at2+vJ598UgMHDlS5cuV09uxZrVixQqdPn9ayZcsUGhqqV155RUOHDtX169fVrl07JSUlaenSpZoxY4amT59us8P97caPH6+hQ4dmeHZeYnk9AAAAADiqPDNDL91KeO/3WfYNGzbIz8/Ppjz+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AAAAAJmMJfe5hK+vr27cuKFPP/1UJj+FAQAAAECuR0LvgNauXStPT09rad++vWrXrq0RI0boueeeU5EiRdSiRQtNnjxZf/zxR3aHCwAAACAPuikjx5bcwjCZznUo4eHh+u233zR37lxrnYeHh/z8/CRJ586d09dff63du3dr9erVOn/+vL755hs98sgjafaXmJioxMREmzqLxSKLxZJ5FwEAQDZZ5xqYZWO1SorLsrEAICfadORadoeQrsaPuGd3CHbBDL0D8vDwULly5awlJZmXpMKFC6t9+/aaOnWqYmNj9dBDD2nKlCnp9hUVFSVvb2+bEhUVlRWXAQAAAAB4AGyKl4u5ubmpbNmyunr1arptIiMjFRERYVPH7DwAAACAB2WauWdpe05FQp9LrF27VsuWLVOnTp1UoUIFmaapzz77TOvXr0/1irvbsbweAAAAABwTCX0uERISovz582vw4MH65ZdfZLFYVL58eb333nvq2rVrdocHAAAAALAzNsUDAAB5BpviAUDW2Xg48e6NskmTR3PHKmU2xQMAAAAAwAGR0AMAAAAA4IB4hh4AAAAAYHem2OU+szFDDwAAAADAXcyZM0elS5eWu7u7qlevrm3btt2x/QcffKBHH31U+fPnl5+fn1544QWdO3fOejwmJkaGYaQq165dy3BMJPQAAAAAANzB8uXLNWjQIL3++us6ePCg6tWrpxYtWuj06dNptt++fbu6deumnj176n//+58+/vhj7du3Ty+++KJNuwIFCig+Pt6muLu7ZzguEnoAAAAAgN3dNHNuuVdvv/22evbsqRdffFHBwcGaPn26/P39NXfu3DTb7969WwEBARo4cKBKly6txx9/XL1799b+/ftt2hmGIV9fX5tyL0joAQAAAAB5SmJioi5fvmxTEhPTfs3e9evXdeDAATVt2tSmvmnTptq5c2ea59SpU0e//vqr1q9fL9M09ccff+iTTz5Rq1atbNpduXJFpUqV0sMPP6zWrVvr4MGD93QdJPQAAAAAgDwlKipK3t7eNiUqKirNtmfPnlVycrKKFy9uU1+8eHElJCSkeU6dOnX0wQcfqGPHjnJzc5Ovr698fHw0a9Ysa5ugoCDFxMRozZo1+uijj+Tu7q66devq+PHjGb4OEnoAAAAAgN2ZppFjS2RkpC5dumRTIiMj73g9hmG7a79pmqnqUhw9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mNATERERERER6SBOuSciIiIiIiLZcT819eMIPREREREREZEOYkJPREREREREpIM45Z6IiIiIiIhkxyn36seEnoiIiCgPaJESo9F4ewzKaCyWpl8bEZGu4JR7IiIiIiIiIh3EEXoiIiIiIiKSXTqn3KsdR+iJiIiIiIiIdBATeiIiIiIiIiIdxCn3REREREREJDtWuVc/jtATERERERER6SAm9EREREREREQ6iAm9DomPj8egQYPg7OwMY2NjFC1aFPXq1cPy5cuRlJQEAHB0dIQkSZAkCaampqhQoQJWrFih5Z4TEREREdG3Jj099x55BdfQ64ibN2/Czc0NVlZWmDZtGipWrIjU1FRcu3YNQUFBsLW1RevWrQEAkyZNQu/evfH69WsEBwejb9++sLKygpeXl5ZfBREREREREcmFCb2O+OWXX6Cvr49z584hX758yvMVK1ZE+/btIT6oOGFubg5ra2sAwJQpU7BlyxaEhIQwoSciIiIiIspDmNDrgISEBISGhmLatGkqyfyHJEnK9vONjY2RkpKiru4RERERERFlwir36sc19Drgxo0bEEKgTJkyKucLFSoEMzMzmJmZYcSIEZk+LzU1FcHBwbh48SK+//57TXWXiIiIiIiINIAj9Drk41H4M2fOID09HZ07d0ZycrLy/IgRIzBmzBgkJyfD0NAQ/v7++Pnnn7NsMzk5WeVzAcDIyAhGRkbyvwAiIiIiIiKSDUfodYCzszMkScLVq1dVzjs5OcHZ2RkmJiYq5/39/REZGYk7d+7g9evXmDVrFhSKrP+rp0+fDktLS5Vj+vTpanstRERERET0bRAi9x55BRN6HVCwYEE0btwYixcvRmJi4n/eX6hQITg7O8PW1vaTa+sBICAgAC9evFA5AgIC5Oo6ERERERERqQkTeh2xdOlSpKamokaNGti8eTOio6MRExOD9evX4+rVq9DT08tRu0ZGRrCwsFA5ON2eiIiIiIgo9+Maeh1RsmRJREREYNq0aQgICMD9+/dhZGQEFxcXDBs2DL/88ou2u0hERERERKSUnoemtudWkhB5aQUBEREREWnCHoMy/32TTFqkxGgsFhHJZ8lf2u5B9vo303YP5MEp90REREREREQ6iFPuiYiIiIiISHa5ezL4p4uH6wqO0BMRERERERHpICb0RERERERERDqIU+6JiIiIiIhIdrl6xn0ewRF6IiIiIiIiIh3EhJ6IiIiIiIhIBzGhJyIiIiIiItJBXENPREREREREsktP13YP8j4m9ERERET0xVqkxGgs1h6DMhqLBWj2tRERfQ1OuSciIiIiIiLSQRyhJyIiIiIiItlx2zr14wg9ERERERERkQ5iQk9ERERERESkgzjlnoiIiIiIiGSXzin3ascReiIiIiIiIiIdxISeiIiIiIiISAdxyj0RERERERHJjlXu1Y8j9Brg7e0NSZIgSRIMDAzg5OSEYcOGITExUXlPnz59oKenh99//z3T50+YMEH5+QqFAra2tujcuTPu3buncl+DBg0wePBglXMLFiyAkZERNm7cqJbXRkRERERERNrBhF5DmjZtiri4ONy8eRNTpkzB0qVLMWzYMABAUlISNm/eDH9/fwQGBmb5+eXLl0dcXBzu37+PzZs34+LFi/jxxx8/GXP8+PEICAjAjh070KlTJ9lfExEREREREWkPp9xriJGREaytrQEAnTp1wqFDhxASEoJly5Zh69atcHFxQUBAAGxsbHD79m04OjqqfL6+vr7y821tbdG7d2/4+vri5cuXsLCwULlXCAFfX1/89ttvCA0NRb169TTyGomIiIiIiDKIXF3mXtJ2B2TBEXotMTExQUpKCgAgMDAQXbp0gaWlJZo3b441a9Z88nPj4+Oxfft26OnpQU9PT+Vaamoqunbtiq1bt+Lw4cNM5omIiIiIiPIojtBrwZkzZ7Bx40Z8//33uH79Ok6dOoXt27cDALp06QJfX1+MHz8eCsX/PW+5ePEizMzMkJ6ejjdv3gAAfH19kS9fPpW2V61aBQC4cOECypYtq6FXRERERERERJrGEXoN2b17N8zMzGBsbIy6deuifv36WLRoEQIDA+Hp6YlChQoBAJo3b47ExET8/fffKp9fpkwZREZG4uzZs5g6dSqqVKmCqVOnZopTr149mJmZYcyYMUhNTf3PfiUnJ+Ply5cqR3JysjwvmoiIiIiIvlnpIvceeQUTeg3x8PBAZGQkYmJi8PbtW2zfvh0FCxbEunXrsGfPHujr60NfXx+mpqZ4+vRppuJ4hoaGcHZ2Rvny5TFq1ChUqVIF/fr1yxSnYsWKOHjwIMLDw/Hjjz8qp/VnZ/r06bC0tFQ5pk+fLutrJyIiIiIiIvlxyr2G5MuXD87Ozirn9u7di1evXiEiIkJlLfzVq1fRuXNnJCQkoGDBglm2N3bsWJQuXRpDhgxBtWrVVK5VqVIFYWFhaNSoETp06ICtW7fCwMAgy3YCAgLg5+encs7IyCgnL5GIiIiIiIg0iCP0WhQYGIgWLVqgcuXKqFChgvJo3749ChcujPXr12f7uU5OTmjTpg3GjRuX5fVKlSrh0KFDOHnyJP73v//h3bt3Wd5nZGQECwsLlYMJPRERERERfS0hcu+RVzCh15JHjx5hz549aN++faZrkiShXbt22e5Jn2Ho0KHYs2cPTp8+neX18uXL49ChQzhz5gzat2+fbVJPREREREREukcSIi89nyAiIiKivGaPQRmNxmuREqPReER51cw/0rXdhWyN+F/eGNvmGnoiIiIiIiKSXXpeKiefS+WNxxJERERERERE3xgm9EREREREREQ6iFPuiYiIiIiISHas1qZ+HKEnIiIiIiIi0kFM6ImIiIiIiIh0EKfcExERERERkew45V79OEJPREREREREpIOY0BMRERERERHpIE65JyIiIqJcrUVKjEbj7TEoo7FYmn5tRJqUzjn3ascReiIiIiIiIiIdxISeiIiIiIiISAdxyj0RERERERHJTqRruwd5H0foiYiIiIiIiHQQE3oiIiIiIiIiHcQp90RERERERCQ7wSr3ascReiIiIiIiIiIdxIReg7y9vSFJEiRJgr6+Puzt7dGvXz88e/YMV69ehSRJOH36tMrn1K5dG0ZGRkhKSlKee/fuHUxNTbFy5Uplu23bts0ULzw8HJIk4fnz5+p8WURERERERKQFTOg1rGnTpoiLi8Pt27exevVq7Nq1C7/88gvKli0LGxsbHDp0SHnv69evERERgSJFiuDEiRPK86dPn8abN2/g4eGhjZdARERERET0n9LTc++RVzCh1zAjIyNYW1ujePHiaNKkCby8vBAaGgoAaNCgAcLDw5X3Hj16FKVLl0br1q1VzoeHh6NYsWIoVaqUhntPREREREREuQUTei26efMm9u3bBwMDAwCAh4cHjh07htTUVADAoUOH0KBBA7i7u6uM3B86dIij80RERERERN84VrnXsN27d8PMzAxpaWl4+/YtAGDu3LkA3o/QJyYm4uzZs6hbty7Cw8Ph7++P+vXro2vXrkhKSoK+vj5OnTqFxYsXZ9nuh9LS0jTzooiIiIiIiD7CKvfqx4Rewzw8PLBs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NUdHRz79IiIiIiIi+sYwoSciIiIiIiLZCVa5VztWuSciIiIiIiLSQUzoiYiIiIiIiHQQp9wTERERERGR7DjlXv04Qk9ERERERESkg5jQExEREREREekgTrknIiIiIiIi2aWLdG13Ic/jCD0RERERERGRDmJCT0RERERERKSDOOWeiOgbcni7q7a7QERE34gWKTEajbfHoIzGYmn6tekqVrlXP47QExEREREREekgJvREREREREREOohT7omIiIiIiEh2nHKvfhyhJyIiIiIiItJBTOiJiIiIiIiIdBCn3BMREREREZHshOCUe3XjCD0RERERERGRDmJCT0RERERERKSDmNDrgFatWqFRo0ZZXjt58iQkScL58+chSZLyyJ8/P+rXr4/Dhw9ruLdERERERERAenp6rj3yCib0OqBnz54ICwvDnTt3Ml0LCgpClSpVUKBAAQDA33//jbi4OBw+fBgWFhZo3rw5bt26pekuExERERERkZoxodcBLVu2RJEiRRAcHKxyPikpCZs3b0bPnj2V5woWLAhra2tUqlQJK1asQFJSEkJDQzXcYyIiIiIiIlI3JvQ6QF9fH926dUNwcLBKpcitW7fi3bt36Ny5c5afZ2pqCgBISUnRSD+JiIiIiIgyiHSRa4+8ggm9jvDx8cHt27cRHh6uPBcUFIR27dohf/78me5PTExEQEAA9PT04O7unm27ycnJePnypcqRnJysjpdAREREREREMmJCryPKli0LV1dXBAUFAQBiY2Nx9OhR+Pj4qNzn6uoKMzMzmJubY9euXQgODkbFihWzbXf69OmwtLRUOaZPn67W10JERERERERfT1/bHaDP17NnTwwYMABLlizBmjVr4ODggO+//17lns2bN8PFxQVWVlYoWLDgf7YZEBAAPz8/lXNGRkay9puIiIiIiL49QuSdavK5FUfodciPP/4IPT09bNy4EWvXrkWPHj0gSZLKPXZ2dihZsuRnJfPA++TdwsJC5WBCT0RERERElPtxhF6HmJmZwcvLC6NGjcKLFy/g7e2t7S4RERERERGRlnCEXsf07NkTz549Q6NGjWBvb6/t7hAREREREWVJ25Xsv4Uq9xyh1zF169ZV2boug6OjY5bniYiIiIiIKG/iCD0RERERERGRDuIIPREREREREckuL01tz604Qk9ERERERESkg5jQExERERER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",
      "text/plain": [
       "<Figure size 1200x1000 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "correlation_matrix = df.corr()\n",
    "# Filter correlation values based on the threshold\n",
    "threshold = 0.75\n",
    "filtered_corr_matrix = correlation_matrix[abs(correlation_matrix) > threshold]\n",
    "\n",
    "# Plot a heatmap of the filtered correlation matrix\n",
    "plt.figure(figsize=(12, 10))\n",
    "sns.heatmap(filtered_corr_matrix, cmap='coolwarm')\n",
    "plt.title(\"Correlation Heatmap (Threshold > 0.85)\")\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(20555, 36)"
      ]
     },
     "execution_count": 61,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 20555 entries, 0 to 20554\n",
      "Data columns (total 35 columns):\n",
      " #   Column           Non-Null Count  Dtype  \n",
      "---  ------           --------------  -----  \n",
      " 0   id               20555 non-null  object \n",
      " 1   type             20555 non-null  object \n",
      " 2   locality         20555 non-null  object \n",
      " 3   latitude         20555 non-null  float64\n",
      " 4   longitude        20555 non-null  float64\n",
      " 5   lease_type       20555 non-null  object \n",
      " 6   furnishing       20555 non-null  object \n",
      " 7   parking          20555 non-null  object \n",
      " 8   property_size    20555 non-null  float64\n",
      " 9   bathroom         20555 non-null  float64\n",
      " 10  facing           20555 non-null  object \n",
      " 11  floor            20555 non-null  float64\n",
      " 12  total_floor      20555 non-null  float64\n",
      " 13  water_supply     20555 non-null  object \n",
      " 14  building_type    20555 non-null  object \n",
      " 15  balconies        20555 non-null  float64\n",
      " 16  rent             20555 non-null  float64\n",
      " 17  LIFT             20555 non-null  int64  \n",
      " 18  GYM              20555 non-null  int64  \n",
      " 19  AC               20555 non-null  int64  \n",
      " 20  CLUB             20555 non-null  int64  \n",
      " 21  INTERCOM         20555 non-null  int64  \n",
      " 22  POOL             20555 non-null  int64  \n",
      " 23  CPA              20555 non-null  int64  \n",
      " 24  FS               20555 non-null  int64  \n",
      " 25  SERVANT          20555 non-null  int64  \n",
      " 26  SECURITY         20555 non-null  int64  \n",
      " 27  GP               20555 non-null  int64  \n",
      " 28  PARK             20555 non-null  int64  \n",
      " 29  RWH              20555 non-null  int64  \n",
      " 30  STP              20555 non-null  int64  \n",
      " 31  HK               20555 non-null  int64  \n",
      " 32  PB               20555 non-null  int64  \n",
      " 33  VP               20555 non-null  int64  \n",
      " 34  age_of_property  20555 non-null  int64  \n",
      "dtypes: float64(8), int64(18), object(9)\n",
      "memory usage: 5.5+ MB\n"
     ]
    }
   ],
   "source": [
    "df.drop(columns=['Unnamed: 0'],inplace=True)\n",
    "df.info()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Chcek Column by column for outliers "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "BHK2        11705\n",
       "BHK3         4388\n",
       "BHK1         3613\n",
       "RK1           553\n",
       "BHK4          233\n",
       "BHK4PLUS       31\n",
       "bhk2           16\n",
       "bhk3           12\n",
       "1BHK1           4\n",
       "Name: type, dtype: int64"
      ]
     },
     "execution_count": 63,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['type'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "BHK2        11721\n",
       "BHK3         4400\n",
       "BHK1         3617\n",
       "RK1           553\n",
       "BHK4          233\n",
       "BHK4PLUS       31\n",
       "Name: type, dtype: int64"
      ]
     },
     "execution_count": 64,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['type'] = df['type'].replace('1BHK1', 'BHK1')\n",
    "df['type'] = df['type'].replace('bhk2', 'BHK2')\n",
    "df['type'] = df['type'].replace('bhk3', 'BHK3')\n",
    "df['type'].value_counts()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "FAMILY      10213\n",
       "ANYONE       9697\n",
       "BACHELOR      587\n",
       "COMPANY        58\n",
       "Name: lease_type, dtype: int64"
      ]
     },
     "execution_count": 65,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['lease_type'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "SEMI_FURNISHED     17950\n",
       "NOT_FURNISHED       1429\n",
       "FULLY_FURNISHED     1176\n",
       "Name: furnishing, dtype: int64"
      ]
     },
     "execution_count": 66,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['furnishing'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "BOTH            10841\n",
       "TWO_WHEELER      7224\n",
       "FOUR_WHEELER     1448\n",
       "NONE             1042\n",
       "Name: parking, dtype: int64"
      ]
     },
     "execution_count": 67,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['parking'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "CORP_BORE      10732\n",
       "CORPORATION     6729\n",
       "BOREWELL        3094\n",
       "Name: water_supply, dtype: int64"
      ]
     },
     "execution_count": 68,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['water_supply'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "IF    9263\n",
       "AP    8876\n",
       "IH    2399\n",
       "GC      17\n",
       "Name: building_type, dtype: int64"
      ]
     },
     "execution_count": 69,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['building_type'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "BHK2        11721\n",
       "BHK3         4400\n",
       "BHK1         3617\n",
       "RK1           553\n",
       "BHK4          233\n",
       "BHK4PLUS       31\n",
       "Name: type, dtype: int64"
      ]
     },
     "execution_count": 70,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['type'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Group by 'locality' and count occurrences\n",
    "locality_counts = df.groupby('locality').size()\n",
    "\n",
    "# Create a boolean mask to filter rows with repeating unique values\n",
    "repeating_unique_mask = df['locality'].map(locality_counts) > 20\n",
    "\n",
    "# Filter the DataFrame to keep only rows wit\n",
    "df = df[repeating_unique_mask]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Whitefield              1502\n",
       "HSR Layout               797\n",
       "Banashankari             746\n",
       "Bellandur                619\n",
       "Marathahalli             527\n",
       "                        ... \n",
       "Chikkakannalli            22\n",
       "Hanumanthnagar            21\n",
       "Thirumalashettyhally      21\n",
       "Yemalur                   21\n",
       "GM Palya                  21\n",
       "Name: locality, Length: 135, dtype: int64"
      ]
     },
     "execution_count": 72,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['locality'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(18932, 35)"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "metadata": {},
   "outputs": [],
   "source": [
    "label_encoder = LabelEncoder()\n",
    "# For lease_type\n",
    "df['lease_type_encoded'] = label_encoder.fit_transform(df['lease_type'])\n",
    "# Drop the original 'lease_type' column\n",
    "df.drop(columns=['lease_type'], inplace=True)\n",
    "\n",
    "#\n",
    "df['furnishing_encoded'] = label_encoder.fit_transform(df['furnishing'])\n",
    "df.drop(columns=['furnishing'], inplace=True)\n",
    "\n",
    "#\n",
    "df['parking_encoded'] = label_encoder.fit_transform(df['parking'])\n",
    "df.drop(columns=['parking'], inplace=True)\n",
    "\n",
    "#\n",
    "df['water_supply_encoded'] = label_encoder.fit_transform(df['water_supply'])\n",
    "df.drop(columns=['water_supply'], inplace=True)\n",
    "\n",
    "#\n",
    "df['building_type_encoded'] = label_encoder.fit_transform(df['building_type'])\n",
    "df.drop(columns=['building_type'], inplace=True)\n",
    "\n",
    "#\n",
    "df['BHK_type_encoded'] = label_encoder.fit_transform(df['type'])\n",
    "df.drop(columns = ['type'], inplace=True)\n",
    "df['locality_encoded'] = label_encoder.fit_transform(df['locality'])\n",
    "df.drop(columns = ['locality'], inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>id</th>\n",
       "      <th>latitude</th>\n",
       "      <th>longitude</th>\n",
       "      <th>property_size</th>\n",
       "      <th>bathroom</th>\n",
       "      <th>facing</th>\n",
       "      <th>floor</th>\n",
       "      <th>total_floor</th>\n",
       "      <th>balconies</th>\n",
       "      <th>rent</th>\n",
       "      <th>...</th>\n",
       "      <th>PB</th>\n",
       "      <th>VP</th>\n",
       "      <th>age_of_property</th>\n",
       "      <th>lease_type_encoded</th>\n",
       "      <th>furnishing_encoded</th>\n",
       "      <th>parking_encoded</th>\n",
       "      <th>water_supply_encoded</th>\n",
       "      <th>building_type_encoded</th>\n",
       "      <th>BHK_type_encoded</th>\n",
       "      <th>locality_encoded</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>ff8081815733a243015733b2876600a6</td>\n",
       "      <td>12.934471</td>\n",
       "      <td>77.634471</td>\n",
       "      <td>1250.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>E</td>\n",
       "      <td>6.0</td>\n",
       "      <td>12.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>40000.0</td>\n",
       "      <td>...</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>5</td>\n",
       "      <td>3</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>131</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>ff8081815ee25e15015ee50004da2acd</td>\n",
       "      <td>12.929557</td>\n",
       "      <td>77.672280</td>\n",
       "      <td>1400.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>NE</td>\n",
       "      <td>3.0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>22000.0</td>\n",
       "      <td>...</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>19</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>ff80818164b68a700164b74b1b247a1d</td>\n",
       "      <td>12.955991</td>\n",
       "      <td>77.531634</td>\n",
       "      <td>600.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>E</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>8000.0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>5</td>\n",
       "      <td>3</td>\n",
       "      <td>2</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>ff80818163b1faf00163b4b9b8a163b1</td>\n",
       "      <td>12.963903</td>\n",
       "      <td>77.649446</td>\n",
       "      <td>1500.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>E</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>45000.0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>5</td>\n",
       "      <td>3</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>2</td>\n",
       "      <td>73</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>ff8081815f48e4aa015f4dd1a9c6696b</td>\n",
       "      <td>12.986196</td>\n",
       "      <td>77.718314</td>\n",
       "      <td>1080.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>E</td>\n",
       "      <td>3.0</td>\n",
       "      <td>5.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>18000.0</td>\n",
       "      <td>...</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>5</td>\n",
       "      <td>3</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>51</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 35 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "                                 id   latitude  longitude  property_size  \\\n",
       "0  ff8081815733a243015733b2876600a6  12.934471  77.634471         1250.0   \n",
       "1  ff8081815ee25e15015ee50004da2acd  12.929557  77.672280         1400.0   \n",
       "3  ff80818164b68a700164b74b1b247a1d  12.955991  77.531634          600.0   \n",
       "4  ff80818163b1faf00163b4b9b8a163b1  12.963903  77.649446         1500.0   \n",
       "5  ff8081815f48e4aa015f4dd1a9c6696b  12.986196  77.718314         1080.0   \n",
       "\n",
       "   bathroom facing  floor  total_floor  balconies     rent  ...  PB  VP  \\\n",
       "0       2.0      E    6.0         12.0        2.0  40000.0  ...   1   1   \n",
       "1       2.0     NE    3.0          4.0        2.0  22000.0  ...   1   1   \n",
       "3       1.0      E    1.0          2.0        0.0   8000.0  ...   0   0   \n",
       "4       3.0      E    0.0          0.0        1.0  45000.0  ...   0   1   \n",
       "5       2.0      E    3.0          5.0        2.0  18000.0  ...   1   0   \n",
       "\n",
       "   age_of_property  lease_type_encoded  furnishing_encoded  parking_encoded  \\\n",
       "0                5                   3                   2                0   \n",
       "1                5                   0                   2                0   \n",
       "3                5                   3                   2                3   \n",
       "4                5                   3                   2                0   \n",
       "5                5                   3                   2                0   \n",
       "\n",
       "   water_supply_encoded  building_type_encoded  BHK_type_encoded  \\\n",
       "0                     2                      0                 1   \n",
       "1                     1                      0                 1   \n",
       "3                     1                      3                 0   \n",
       "4                     1                      3                 2   \n",
       "5                     2                      0                 0   \n",
       "\n",
       "   locality_encoded  \n",
       "0               131  \n",
       "1                19  \n",
       "3                 4  \n",
       "4                73  \n",
       "5                51  \n",
       "\n",
       "[5 rows x 35 columns]"
      ]
     },
     "execution_count": 74,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1200.0    1571\n",
       "600.0     1241\n",
       "1000.0    1122\n",
       "800.0      920\n",
       "1100.0     805\n",
       "          ... \n",
       "582.0        1\n",
       "1617.0       1\n",
       "1219.0       1\n",
       "1269.0       1\n",
       "415.0        1\n",
       "Name: property_size, Length: 1097, dtype: int64"
      ]
     },
     "execution_count": 75,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['property_size'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAApIAAAIhCAYAAAD91lq9AAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/YYfK9AAAACXBIWXMAAA9hAAAPYQGoP6dpAAAxCUlEQVR4nO3dd5hV1b344e8MDENHFBQQpIiICmKEKGCugBgVhFhjQyUa7DVG41VjxBsjllzjTSLGqAEVg5oL9hJJrijq2ChRBI1GKUqzURRByvr9kd+cZBxAWNIG3/d5zvMwe6+z9zpnCfN5zjn7WJRSSgEAAOuoeFNPAACAqklIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSEIVM3z48CgqKqpwa9y4cfTs2TMeeeSRjT6fsWPHVphLtWrVYrvttovvf//7MXXq1MK4adOmRVFRUQwfPnydzzFlypQYPHhwTJs2bf1N/P/761//Gl26dIk6depEUVFRPPDAA6scVz7/8ltxcXFss8020bdv3ygrK1vv89qYrr766tU+7q9j5syZceaZZ0a7du2iVq1asfXWW0fHjh3jlFNOiZkzZxbGDR48OIqKitb7+YENT0hCFTVs2LAoKyuL559/Pn7/+99HtWrVon///vHwww9vkvlcffXVUVZWFk899VRcfPHFMWbMmNhnn33i/fff/9rHnjJlSlx55ZXrPSRTSnHUUUdFSUlJPPTQQ1FWVhY9evRY433OOeecKCsri3HjxsWQIUPib3/7W/Tq1SsmTpy4Xue2MW2IkHzvvfdizz33jDFjxsQFF1wQjz32WPzhD3+IY489Nl5++eV45513CmMHDRpU5WMcvqmqb+oJAHk6dOgQXbp0Kfx80EEHRcOGDWPkyJHRv3//jT6fnXbaKbp27RoREfvuu29stdVW8cMf/jCGDx8el1122Uafz9qYNWtWfPzxx3HYYYdF79691+o+O+ywQ+Fx7rPPPtG2bdvo3bt3DB06NG699dZV3ufzzz+PmjVrbnavun3++edRq1atDXLsW2+9NT788MN46aWXonXr1oXthx56aFx66aWxcuXKwrbmzZtH8+bNN8g8gA3LK5KwhahZs2bUqFEjSkpKKmz/+OOP48wzz4ztt98+atSoEW3atInLLrssli5dGhERS5YsiW9961vRtm3bWLBgQeF+c+bMiSZNmkTPnj1jxYoV6zyf8tiaPn36Gsc9++yz0bt376hXr17Url07unfvHo8++mhh//Dhw+P73/9+RET06tWr8NbyV71F/lXHHTx4cCFeLr744igqKopWrVp97cdZ/tGDJ598Mk4++eRo3Lhx1K5dO5YuXRorV66M6667Ltq3bx+lpaWx7bbbxoknnhjvvfdehWP27NkzOnToEOPGjYuuXbtGrVq1Yvvtt4/LL7+80lp88cUXcdVVVxWO2bhx4zjppJPigw8+qDCuVatW0a9fvxg9enR861vfipo1a8aVV14ZRUVF8dlnn8Udd9xReG579uwZ06ZNi+rVq8eQIUMqPeZnnnkmioqK4k9/+tNqn5ePPvooiouLY9ttt13l/uLif/36+fJb26v6+Ma/z61cSimGDh0ae+yxR9SqVSsaNmwYRx55ZIVXO4ENS0hCFbVixYpYvnx5LFu2LN577704//zz47PPPovjjjuuMGbJkiXRq1evuPPOO+OCCy6IRx99NI4//vi47rrr4vDDD4+IfwbofffdF/PmzYuTTz45IiJWrlwZAwYMiJRSjBw5MqpVq7bO83v77bcjIqJx48arHfP000/HfvvtFwsWLIjbb789Ro4cGfXq1Yv+/fvHvffeGxERBx98cFx99dUREXHTTTdFWVlZlJWVxcEHH/y1jjto0KAYPXp0RPzr7er7779/vT3Ok08+OUpKSuKuu+6K//3f/42SkpI444wz4uKLL47vfve78dBDD8XPf/7zeOKJJ6J79+7x4YcfVrj/nDlz4phjjokBAwbEgw8+GEceeWRcddVVcd555xXGrFy5Mg455JC45ppr4rjjjotHH300rrnmmhgzZkz07NkzPv/88wrHnDBhQlx00UVx7rnnxhNPPBFHHHFElJWVRa1atQqf9SwrK4uhQ4dGq1at4nvf+1787ne/qxSvv/3tb6NZs2Zx2GGHrfZ56datW6xcuTIOP/zw+POf/xwLFy5c6+f04IMPLsyl/HbDDTdERMRuu+1WGHfaaafF+eefH/vvv3888MADMXTo0Hj99deje/fuMXfu3LU+H/A1JKBKGTZsWIqISrfS0tI0dOjQCmN/97vfpYhI9913X4Xt1157bYqI9OSTTxa23XvvvSki0o033ph+9rOfpeLi4gr7V+epp55KEZHuvffetGzZsrR48eL0zDPPpLZt26Zq1aqlv/3tbymllN59990UEWnYsGGF+3bt2jVtu+22adGiRYVty5cvTx06dEjNmzdPK1euTCml9Kc//SlFRHrqqafW6jla2+OWz+n666//ymOWj7322mvTsmXL0pIlS9L48ePTt7/97RQR6dFHH00p/Wt9TjzxxAr3nzp1aoqIdOaZZ1bY/uKLL6aISJdeemlhW48ePVJEpAcffLDC2FNOOSUVFxen6dOnp5RSGjlyZIqINGrUqArjXn755RQRFf57aNmyZapWrVp68803Kz22OnXqpIEDB1baXr62999/f2Hb+++/n6pXr56uvPLKNTxbKa1cuTKddtppqbi4OEVEKioqSrvsskv60Y9+lN59990KY6+44oq0pl9Hb7zxRtpmm21Sr1690tKlS1NKKZWVlaWISP/93/9dYezMmTNTrVq10k9+8pM1zg9YP4QkVDHloXLnnXeml19+Ob388svp8ccfT6eeemoqKipKv/nNbwpjjzrqqFSnTp1COJWbO3duioh08cUXV9h+xhlnpJKSklRcXJx++tOfrtV8ymPjy7fWrVtXCJAvh+Snn36aioqKKoVVSv8K3alTp6aU1i0k1+W4OSH55dt2222XbrnllsK48vX5cgQOHTo0RUR66aWXKh17l112SXvvvXfh5x49eqR69epVGlf+XN91110ppZQGDBiQttpqq/TFF1+kZcuWVbg1adIkHXXUUYX7tmzZMn3rW99a5WNbXUimlFKnTp3S/vvvX/j58ssvTyUlJWn27NmrHP9l06ZNS0OHDk0nn3xyatu2bYqIVLt27TR27NjCmDWF5OzZs1OrVq1Shw4d0vz58wvbL7vsslRUVJTmzp1b6bF37do17bXXXms1P+DrcbENVFG77LJLpYttpk+fHj/5yU/i+OOPj6222io++uijaNKkSaWLPLbddtuoXr16fPTRRxW2n3zyyXHzzTdHjRo14txzz12n+Vx77bWx3377RbVq1aJRo0bRokWLNY7/5JNPIqUUTZs2rbSvWbNmERGV5rc2NtRxy5133nlx/PHHR3FxcWy11VbRunXrVV5E8+Xzl59zdfP68mdJt9tuu0rjmjRpUuFYc+fOjfnz50eNGjVWOdcvv12+qnN/lXPPPTcGDRoUb775ZrRp0yZuvfXWOPLIIwtz+SotW7aMM844o/DzfffdF8cee2xcdNFF8dJLL63xvosWLYq+ffvGsmXL4vHHH48GDRoU9s2dOzdSSqt8niIi2rRps1bzA74eIQlbkN133z3+/Oc/x9///vfYa6+9YptttokXX3wxUkoVYmfevHmxfPnyaNSoUWHbZ599FieccEK0a9cu5s6dG4MGDYoHH3xwrc/dpk2bCmH7VRo2bBjFxcUxe/bsSvtmzZoVEVFhfpv6uOWaN2++Vo/zy3G5zTbbRETE7NmzK12hPGvWrEpzWtVn/ObMmVPhWI0aNYptttkmnnjiiVXOoV69emuc09o47rjj4uKLL46bbropunbtGnPmzImzzjprnY9T7qijjoohQ4bE5MmT1zhu2bJlccQRR8Q//vGPGDduXKXnrFGjRlFUVBTjxo2L0tLSSvdf1TZg/XOxDWxBJk2aFBH/uvCjd+/e8emnn1b6jsA777yzsL/c6aefHjNmzIjRo0fH7bffHg899FD86le/2mBzrVOnTuy9994xevToCheFrFy5MkaMGBHNmzePdu3aRcS/ouDLF4983eNuTPvtt19ERIwYMaLC9pdffjmmTp1a6euHFi1aFA899FCFbX/84x+juLg49t1334iI6NevX3z00UexYsWK6NKlS6XbzjvvvFZzKy0tXe1zW7NmzTj11FPjjjvuiBtuuCH22GOP2Geffb7ymKsK+YiITz/9NGbOnFl4dXh1fvjDH8bYsWNj9OjRsfvuu1fa369fv0gpxfvvv7/Kx96xY8evnCPw9XlFEqqoyZMnx/LlyyPin291jh49OsaMGROHHXZY4Xv7TjzxxLjpppti4MCBMW3atOjYsWM8++yzcfXVV0ffvn1j//33j4iI2267LUaMGBHDhg2L3XbbLXbbbbc4++yz4+KLL4599tkn9tprrw3yGIYMGRLf/e53o1evXnHhhRdGjRo1YujQoTF58uQYOXJk4RW0Dh06RETE73//+6hXr17UrFkzWrduXXhlLve4G9POO+8cp556avzmN7+J4uLi6NOnT0ybNi0uv/zyaNGiRfzoRz+qMH6bbbaJM844I2bMmBHt2rWLxx57LG699dY444wzYocddoiIiGOOOSbuvvvu6Nu3b5x33nmx1157RUlJSbz33nvx1FNPxSGHHLLGK6vLdezYMcaOHRsPP/xwNG3aNOrVq1chQs8888y47rrrYvz48XHbbbet1eP9xS9+Ec8991wcffTRha/neffdd+O3v/1tfPTRR3H99dev9r7XX3993HXXXXHOOedEnTp14oUXXijsq1+/fuy6666xzz77xKmnnhonnXRSvPLKK7HvvvtGnTp1Yvbs2fHss89Gx44dK7ylDmwgm/QTmsA6W9VV2w0aNEh77LFHuuGGG9KSJUsqjP/oo4/S6aefnpo2bZqqV6+eWrZsmS655JLCuFdffTXVqlWr0sUWS5YsSZ07d06tWrVKn3zyyWrnU34ByJ/+9Kc1zntVV22nlNK4cePSfvvtl+rUqZNq1aqVunbtmh5++OFK97/xxhtT69atU7Vq1VZ5nC9bm+PmXGzzVWPL1+fll1+utG/FihXp2muvTe3atUslJSWpUaNG6fjjj08zZ86sMK5Hjx5pt912S2PHjk1dunRJpaWlqWnTpunSSy9Ny5YtqzB22bJl6Ze//GXq1KlTqlmzZqpbt25q3759Ou2009Jbb71VGNeyZct08MEHr3LOkyZNSvvss0+qXbt2iojUo0ePSmN69uyZtt5667R48eI1Pv5yL7zwQjrrrLNSp06d0tZbb52qVauWGjdunA466KD02GOPVRj75YttBg4cuMoLm1Y1tz/84Q9p7733LqzzjjvumE488cT0yiuvrNU8ga+nKKWUNna8ArB6PXv2jA8//PArP0e4scybNy9atmwZ55xzTlx33XWbejrAZsRb2wCs0nvvvRfvvPNOXH/99VFcXFzhy9ABIlxsA8Bq3HbbbdGzZ894/fXX4+67747tt99+U08J2Mx4axsAgCxekQQAIIuQBAAgi5AEACDLRr9qe+XKlTFr1qyoV6/eJvlSYAAA1iylFIsWLYpmzZpFcfHqX3fc6CE5a9asaNGixcY+LQAA62jmzJmV/l/3/26jh2S9evUi4p8Tq1+//sY+PQAAX2HhwoXRokWLQretzkYPyfK3s+vXry8kAQA2Y1/1MUQX2wAAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJCl+qaewObgrbfeikWLFkVERNHyJVHz0xmxpO4OUbdh49hpp5028ewAADZP3/iQfOutt6Jdu3aFn7/VpDgmnFY39rzl05g4Z2X8/e9/F5MAAKvwjX9ru/yVyBEjRsT48ePj7rvvjoiIq666qsJ+AAAq+sa/Illul112iT333DNiVnHEMxGtW7fe1FMCANisfeNfkQQAII+QBAAgi5AEACCLkAQAIIuQBAAgi5AEACCLkAQAIIuQBAAgi5AEACCLkAQAIIuQBAAgi5AEACCLkAQAIMsWH5KLFy+OCRMmxOLFi6vk8QEANldbfEi+8cYb0blz53jjjTeq5PEBADZXW3xIAgCwYQhJAACyCEkAALIISQAAsghJAACyCEkAALIISQAAsghJAACyCEkAALIISQAAsghJAACyCEkAALJU39QTqMpWrFgRhx9+eEREdO7c+Wsdq0mTJnHQQQfFjBkz4p133onatWtHgwYNYp999omSkpKYP39+FBUVxU477RRnnnlm1KhRI1asWBHjxo2L2bNnx7bbbhsREXPmzIkPPvggGjduHNtvv338x3/8R1SrVq0w3/LxTZs2rbBvc7e+574ux6vKzxsAVdtm/zsoraOnn3469evXLzVt2jRFRLr//vvX6f4LFixIEZEWLFiwrqfOMn78+BQRafz48Wu3//2JKV1RP03568g13m/UqFEpIjbJrXr16umQQw5JrVq1+sqxrVq1SqNGjUqjRo2qNL583+Zufc99XY5XlZ83AKq2Tfk7aG17bZ3f2v7ss8+iU6dO8dvf/nZd77rFGD16dBxxxBEb9ZylpaWFP9eoUSMefPDBqFatWgwZMiSKioqiffv2hf1nnHFG9OnTJyIiGjVqFEcccUQceeSR0bFjxygrK4tFixZFWVlZdOzYMY488sgYPXr0Rn0s62L06NHrde7rcrz1fW4AWFtV5nfQ16nV+Aa+Irl8+fKN8qpjz549K23r06dPql27diouLk41atRI1apVSy1btkz9+vVLrVq1Sv369Uv9+vVLrVu3Tl988UXq379/atmyZapVq1aqXbt2+uKLLyo8lhUrVqT+/fun1q1bp+XLl2+Ip/9rWb58eWrVqlXq379/WrFiRYV9OXNfl+Ot73MDwNraHH4HrW2vbfDPSC5dujSWLl1a+HnhwoUb+pQVfP755xERMXXq1FXuL99ePq5c+Zy/fL9XXnllfU9xlcaPH1/480477RRvvfVWfPbZZ7F48eKIiDjiiCNi5MiRMX369PjJT34SjzzySIwcOTJSStG9e/d47rnn4pJLLonu3bsXjvPcc89Fz549Cz8XFxcXxowbN67Cvs3BuHHjYtq0aTFy5MgoLq744nnO3NfleBGxXs8NAGtrff/+25A2eEgOGTIkrrzyyg19mtWaNm1aREQcf/zxXzlun332Kfw8a9astbrfhvLvYbv11ltHRMSHH35Y2NalS5cYOXJkRETUqlUrIiI6dOgQKaWIiJg9e3b069evwjFnz55d6TwdOnRY7b5NrXxO5XP8snWde87x1te5AWBtre/ffxvSBv/6n0suuSQWLFhQuM2cOXNDn7KCVq1aRUTEiBEjYvz48ZVuI0aMqDCuXLNmzVZ5v1tuuWWjzLs8DiMiPv7444j45+cdy/37K6Pl0Tl58uSYPHlyREQ0bdq08OdyTZs2rXSefx+/uSmf05cfR7l1nfu6HG99nxsA1laV+h30dd4/D5+R9BnJDchnJAH4Jtocfgetba8JyYyv/9kUX/1To0aNwp9r166dIiLtuOOO6eqrr05FRUWpffv2hf2nn3566tOnT4qI1KVLlxQRqaioKPXv3z89//zzaeHChen5559P/fv3T0VFRZv1V9mMGjVqvc59XY63vs8NAGtrU/8O2mAhuWjRojRx4sQ0ceLEFBHphhtuSBMnTkzTp09frxNbX77p3yPZunXr1X6PZPm+zd36nvu6HK8qP28AVG2b8nfQ2vZaUUr//+qMtTR27Njo1atXpe0DBw6M4cOHf+X9Fy5cGA0aNIgFCxZE/fr11+XUWSZMmBCdO3eO8ePHx5577vnV+2dNivh9j5i67y2xa+9jV3u/iH9+2/yOO+4Y06dP/9rz9H+2WTP/ZxsAvok21e+gte21db5qu2fPnrGO7bnFqlatWowePXqNobqhz78ul/2v6/jNyfqe+7ocryo/bwBUbZv776ANftU2AABbJiEJAEAWIQkAQBYhCQBAFiEJAEAWIQkAQBYhCQBAFiEJAEAWIQkAQBYhCQBAFiEJAECWLT4k27dvH+PHj4/27dtXyeMDAGyuqm/qCWxotWvXjj333LPKHh8AYHO1xb8iCQDAhiEkAQDIIiQBAMgiJAEAyCIkAQDIIiQBAMgiJAEAyCIkAQDIIiQBAMgiJAEAyCIkAQDIIiQBAMgiJAEAyFJ9U09gU1u8eHFEREyYMCEiImrN/3vsEhHvvvvuJpwVAMDm7xsfkm+88UZERJxyyikREfGtJsUx4bS68dOf/jQiIurVq7fJ5gYAsDn7xofkoYceGhER7du3j9q1a0fR8iUx9dMZcXvfHaJuw8ax0047bdoJAgBspopSSmljnnDhwoXRoEGDWLBgQdSvX39jnhoAgLWwtr3mYhsAALIISQAAsghJAACyCEkAALIISQAAsghJAACyCEkAALIISQAAsghJAACyCEkAALIISQAAsghJAACyCEkAALIISQAAsghJAACyCEkAALIISQAAsghJAACyCEkAALIISQAAsghJAACyCEkAALIISQAAsghJAACyCEkAALIISQAAsghJAACyCEkAALIISQAAsghJAACyCEkAALIISQAAsghJAACyCEkAALIISQAAsghJAACyCEkAALIISQAAsghJAACyCEkAALIISQAAsghJAACyCEkAALIISQAAsghJAACyCEkAALIISQAAsghJAACyCEkAALIISQAAsghJAACyCEkAALIISQAAsghJAACyCEkAALIISQAAsghJAACyCEkAALIISQAAsghJAACyCEkAALIISQAAsghJAACyCEkAALIISQAAsghJAACyCEkAALIISQAAsghJAACyCEkAALIISQAAsghJAACyCEkAALIISQAAsghJAACyCEkAALIISQAAsghJAACyCEkAALIISQAAsghJAACyCEkAALIISQAAsghJAACyCEkAALIISQAAsghJAACyCEkAALIISQAAsghJAACyCEkAALIISQAAsghJAACyCEkAALIISQAAsghJAACyCEkAALIISQAAsghJAACyCEkAALIISQAAsghJAACyCEkAALIISQAAsghJAACyCEkAALIISQAAsghJAACyCEkAALIISQAAsghJAACyCEkAALIISQAAsghJAACyCEkAALIISQAAsghJAACyCEkAALIISQAAsghJAACyCEkAALIISQAAsghJAACyCEkAALIISQAAsghJAACyCEkAALIISQAAsghJAACyCEkAALIISQAAsghJAACyCEkAALIISQAAsghJAACyCEkAALIISQAAsghJAACyCEkAALIISQAAsghJAACyCEkAALIISQAAsghJAACyCEkAALIISQAAsghJAACyCEkAALIISQAAsghJAACyCEkAALIISQAAsghJAACyCEkAALIISQAAsghJAACyCEkAALIISQAAsghJAACyCEkAALIISQAAsghJAACyCEkAALIISQAAsghJAACyCEkAALIISQAAsghJAACyCEkAALIISQAAsghJAACyCEkAALIISQAAsghJAACyCEkAALIISQAAsghJAACyCEkAALIISQAAsghJAACyCEkAALIISQAAsghJAACyCEkAALIISQAAsghJAACyCEkAALIISQAAsghJAACyCEkAALIISQAAsghJAACyCEkAALJU39gnTClFRMTChQs39qkBAFgL5Z1W3m2rs9FDctGiRRER0aJFi419agAA1sGiRYuiQYMGq91flL4qNdezlStXxqxZs6JevXpRVFS0wc+3cOHCaNGiRcycOTPq16+/wc/H+mX9qj5rWPVZw6rPGlZtm2L9UkqxaNGiaNasWRQXr/6TkBv9Fcni4uJo3rz5xj5t1K9f31+eKsz6VX3WsOqzhlWfNazaNvb6remVyHIutgEAIIuQBAAgyxYfkqWlpXHFFVdEaWnppp4KGaxf1WcNqz5rWPVZw6ptc16/jX6xDQAAW4Yt/hVJAAA2DCEJAEAWIQkAQBYhCQBAli06JIcOHRqtW7eOmjVrRufOnWPcuHGbekrfCM8880z0798/mjVrFkVFRfHAAw9U2J9SisGDB0ezZs2iVq1a0bNnz3j99dcrjFm6dGmcc8450ahRo6hTp05873vfi/fee6/CmE8++SROOOGEaNCgQTRo0CBOOOGEmD9/foUxM2bMiP79+0edOnWiUaNGce6558YXX3yxIR72FmPIkCHx7W9/O+rVqxfbbrttHHroofHmm29WGGMNN28333xz7L777oUvL+7WrVs8/vjjhf3Wr2oZMmRIFBUVxfnnn1/YZg03b4MHD46ioqIKtyZNmhT2b1Hrl7ZQ99xzTyopKUm33nprmjJlSjrvvPNSnTp10vTp0zf11LZ4jz32WLrsssvSqFGjUkSk+++/v8L+a665JtWrVy+NGjUqvfbaa+noo49OTZs2TQsXLiyMOf3009P222+fxowZkyZMmJB69eqVOnXqlJYvX14Yc9BBB6UOHTqk559/Pj3//POpQ4cOqV+/foX9y5cvTx06dEi9evVKEyZMSGPGjEnNmjVLZ5999gZ/DqqyAw88MA0bNixNnjw5TZo0KR188MFphx12SJ9++mlhjDXcvD300EPp0UcfTW+++WZ6880306WXXppKSkrS5MmTU0rWryp56aWXUqtWrdLuu++ezjvvvMJ2a7h5u+KKK9Juu+2WZs+eXbjNmzevsH9LWr8tNiT32muvdPrpp1fY1r59+/Sf//mfm2hG30xfDsmVK1emJk2apGuuuaawbcmSJalBgwbpd7/7XUoppfnz56eSkpJ0zz33FMa8//77qbi4OD3xxBMppZSmTJmSIiK98MILhTFlZWUpItIbb7yRUvpn0BYXF6f333+/MGbkyJGptLQ0LViwYIM83i3RvHnzUkSkp59+OqVkDauqhg0bpttuu836VSGLFi1KO+20UxozZkzq0aNHISSt4ebviiuuSJ06dVrlvi1t/bbIt7a/+OKLGD9+fBxwwAEVth9wwAHx/PPPb6JZERHx7rvvxpw5cyqsTWlpafTo0aOwNuPHj49ly5ZVGNOsWbPo0KFDYUxZWVk0aNAg9t5778KYrl27RoMGDSqM6dChQzRr1qww5sADD4ylS5fG+PHjN+jj3JIsWLAgIiK23nrriLCGVc2KFSvinnvuic8++yy6detm/aqQs846Kw4++ODYf//9K2y3hlXDW2+9Fc2aNYvWrVvHMcccE++8805EbHnrV329HGUz8+GHH8aKFStiu+22q7B9u+22izlz5myiWRERhed/VWszffr0wpgaNWpEw4YNK40pv/+cOXNi2223rXT8bbfdtsKYL5+nYcOGUaNGDf8drKWUUlxwwQXxne98Jzp06BAR1rCqeO2116Jbt26xZMmSqFu3btx///2x6667Fn7BWL/N2z333BMTJkyIl19+udI+fwc3f3vvvXfceeed0a5du5g7d25cddVV0b1793j99de3uPXbIkOyXFFRUYWfU0qVtrFp5KzNl8esanzOGFbv7LPPjldffTWeffbZSvus4eZt5513jkmTJsX8+fNj1KhRMXDgwHj66acL+63f5mvmzJlx3nnnxZNPPhk1a9Zc7ThruPnq06dP4c8dO3aMbt26xY477hh33HFHdO3aNSK2nPXbIt/abtSoUVSrVq1Sbc+bN69SmbNxlV+1tqa1adKkSXzxxRfxySefrHHM3LlzKx3/gw8+qDDmy+f55JNPYtmyZf47WAvnnHNOPPTQQ/HUU09F8+bNC9utYdVQo0aNaNu2bXTp0iWGDBkSnTp1iv/5n/+xflXA+PHjY968edG5c+eoXr16VK9ePZ5++un49a9/HdWrVy88d9aw6qhTp0507Ngx3nrrrS3u7+AWGZI1atSIzp07x5gxYypsHzNmTHTv3n0TzYqIiNatW0eTJk0qrM0XX3wRTz/9dGFtOnfuHCUlJRXGzJ49OyZPnlwY061bt1iwYEG89NJLhTEvvvhiLFiwoMKYyZMnx+zZswtjnnzyySgtLY3OnTtv0MdZlaWU4uyzz47Ro0fH//3f/0Xr1q0r7LeGVVNKKZYuXWr9qoDevXvHa6+9FpMmTSrcunTpEgMGDIhJkyZFmzZtrGEVs3Tp0pg6dWo0bdp0y/s7uF4u2dkMlX/9z+23356mTJmSzj///FSnTp00bdq0TT21Ld6iRYvSxIkT08SJE1NEpBtuuCFNnDix8NVL11xzTWrQoEEaPXp0eu2119Kxxx67yq89aN68efrLX/6SJkyYkPbbb79Vfu3B7rvvnsrKylJZWVnq2LHjKr/2oHfv3mnChAnpL3/5S2revLmvrfgKZ5xxRmrQoEEaO3Zsha+uWLx4cWGMNdy8XXLJJemZZ55J7777bnr11VfTpZdemoqLi9OTTz6ZUrJ+VdG/X7WdkjXc3P34xz9OY8eOTe+880564YUXUr9+/VK9evUKDbIlrd8WG5IppXTTTTelli1bpho1aqQ999yz8PUlbFhPPfVUiohKt4EDB6aU/vnVB1dccUVq0qRJKi0tTfvuu2967bXXKhzj888/T2effXbaeuutU61atVK/fv3SjBkzKoz56KOP0oABA1K9evVSvXr10oABA9Inn3xSYcz06dPTwQcfnGrVqpW23nrrdPbZZ6clS5ZsyIdf5a1q7SIiDRs2rDDGGm7eTj755MK/fY0bN069e/cuRGRK1q8q+nJIWsPNW/n3QpaUlKRmzZqlww8/PL3++uuF/VvS+hWllNL6eW0TAIBvki3yM5IAAGx4QhIAgCxCEgCALEISAIAsQhIAgCxCEgCALEISAIAsQhIAgCxCEqCKGTx4cOyxxx6behoAQhLY/PzgBz+IoqKiKCoqipKSkmjTpk1ceOGF8dlnn23qqa3W8OHDY6uttlovxxo1alTsvffe0aBBg6hXr17stttu8eMf/7iw/8ILL4y//vWv6+VcAF9H9U09AYBVOeigg2LYsGGxbNmyGDduXAwaNCg+++yzuPnmmyuNXbZsWZSUlGyCWf7r/OvLX/7ylzjmmGPi6quvju9973tRVFQUU6ZMqRCOdevWjbp16663cwLk8ooksFkqLS2NJk2aRIsWLeK4446LAQMGxAMPPBAR/3pr9w9/+EO0adMmSktLI6UUM2bMiEMOOSTq1q0b9evXj6OOOirmzp1bOGb5/W655ZZo0aJF1K5dO77//e/H/PnzK5x72LBhscsuu0TNmjWjffv2MXTo0MK+adOmRVFRUdx3333Rs2fPqFmzZowYMSJOOumkWLBgQeGV1MGDB8d//dd/RceOHSs9ts6dO8fPfvazVT7uRx55JL7zne/ERRddFDvvvHO0a9cuDj300PjNb35T6XGUKz/nv99atWpV2D9lypTo27dv1K1bN7bbbrs44YQT4sMPP1yH1QBYNSEJVAm1atWq8Mrf22+/Hffdd1+MGjUqJk2aFBERhx56aHz88cfx9NNPx5gxY+If//hHHH300RWOU36/hx9+OJ544omYNGlSnHXWWYX9t956a1x22WXxi1/8IqZOnRpXX311XH755XHHHXdUOM7FF18c5557bkydOjV69+4dN954Y9SvXz9mz54ds2fPjgsvvDBOPvnkmDJlSrz88suF+7366qsxceLE+MEPfrDKx9mkSZN4/fXXY/LkyWv93JSfc/bs2fH2229H27ZtY9999y3s69GjR+yxxx7xyiuvxBNPPBFz586No446aq2PD7BaCWAzM3DgwHTIIYcUfn7xxRfTNttsk4466qiUUkpXXHFFKikpSfPmzSuMefLJJ1O1atXSjBkzCttef/31FBHppZdeKtyvWrVqaebMmYUxjz/+eCouLk6zZ89OKaXUokWL9Mc//rHCfH7+85+nbt26pZRSevfdd1NEpBtvvLHCmGHDhqUGDRpUeix9+vRJZ5xxRuHn888/P/Xs2XO1j/3TTz9Nffv2TRGRWrZsmY4++uh0++23pyVLlhTGXHHFFalTp06V7rty5cp02GGHpc6dO6fFixenlFK6/PLL0wEHHFBh3MyZM1NEpDfffHO18wBYG16RBDZLjzzySNStWzdq1qwZ3bp1i3333bfC27stW7aMxo0bF36eOnVqtGjRIlq0aFHYtuuuu8ZWW20VU6dOLWzbYYcdonnz5oWfu3XrFitXrow333wzPvjgg5g5c2b88Ic/LHwOsW7dunHVVVfFP/7xjwrz69Kly1o9jlNOOSVGjhwZS5YsiWXLlsXdd98dJ5988mrH16lTJx599NF4++2346c//WnUrVs3fvzjH8dee+0VixcvXuO5Lr300igrK4sHHnggatWqFRER48ePj6eeeqrC42nfvn1ERKXHBLCuXGwDbJZ69eoVN998c5SUlESzZs0qXUxTp06dCj+nlKKoqKjScVa3vVz5vqKioli5cmVE/PPt7b333rvCuGrVqq3x/KvTv3//KC0tjfvvvz9KS0tj6dKlccQRR3zl/XbcccfYcccdY9CgQXHZZZdFu3bt4t57742TTjppleNHjBgRv/rVr2Ls2LEVQnnlypXRv3//uPbaayvdp2nTpmv1GABWR0gCm6U6depE27Zt13r8rrvuGjNmzIiZM2cWXpWcMmVKLFiwIHbZZZfCuBkzZsSsWbOiWbNmERFRVlYWxcXF0a5du9huu+1i++23j3feeScGDBiwTvOtUaNGrFixotL26tWrx8CBA2PYsGFRWloaxxxzTNSuXXudjt2qVauoXbv2ar/+qKysLAYNGhS33HJLdO3atcK+PffcM0aNGhWtWrWK6tX9kw+sX/5VAbYI+++/f+y+++4xYMCAuPHGG2P58uVx5plnRo8ePSq8DV2zZs0YOHBg/PKXv4yFCxfGueeeG0cddVQ0adIkIv55RfS5554b9evXjz59+sTSpUvjlVdeiU8++SQuuOCC1Z6/VatW8emnn8Zf//rX6NSpU9SuXbsQjIMGDSrE7HPPPbfGxzF48OBYvHhx9O3bN1q2bBnz58+PX//617Fs2bL47ne/W2n8nDlz4rDDDotjjjkmDjzwwJgzZ05E/PMV1MaNG8dZZ50Vt956axx77LFx0UUXRaNGjeLtt9+Oe+65J2699dZKr7QCrAufkQS2CEVFRfHAAw9Ew4YNY9999439998/2rRpE/fee2+FcW3bto3DDz88+vbtGwcccEB06NChwtf7DBo0KG677bYYPnx4dOzYMXr06BHDhw+P1q1br/H83bt3j9NPPz2OPvroaNy4cVx33XWFfTvttFN07949dt5550pvmX9Zjx494p133okTTzwx2rdvH3369Ik5c+bEk08+GTvvvHOl8W+88UbMnTs37rjjjmjatGnh9u1vfzsiIpo1axbPPfdcrFixIg488MDo0KFDnHfeedGgQYMoLvYrAPh6ilJKaVNPAmBjGDx4cDzwwAOFrwvaWFJK0b59+zjttNPW+KomQFXjrW2ADWjevHlx1113xfvvv7/aC2UAqiohCbABbbfddtGoUaP4/e9/Hw0bNtzU0wFYr7y1DQBAFp+0BgAgi5AEACCLkAQAIIuQBAAgi5AEACCLkAQAIIuQBAAgi5AEACDL/wOivnVxm9016QAAAABJRU5ErkJggg==",
      "text/plain": [
       "<Figure size 800x600 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Create a box plot\n",
    "plt.figure(figsize=(8, 6))\n",
    "plt.boxplot(df['property_size'], vert=False)\n",
    "plt.title('Box Plot of Property Size')\n",
    "plt.xlabel('Property Size')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Remove the outliers\n",
    "Q1 = df['property_size'].quantile(0.25)\n",
    "Q3 = df['property_size'].quantile(0.75)\n",
    "IQR = Q3 - Q1\n",
    "#Identify and print outliers \n",
    "df = df[(df['property_size'] >= Q1 - 1.5 * IQR) & (df['property_size'] <= Q3 + 1.5 * IQR)]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAApIAAAIhCAYAAAD91lq9AAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/YYfK9AAAACXBIWXMAAA9hAAAPYQGoP6dpAAAuzUlEQVR4nO3deZxWZf34//cMDMM2oLINCAIuCAniloL2FVwTxFwyXFBJRXHXXPKTZmKZC5b5KaUUDVzIpURzi6QC11FxyxQ0TRGULVFZZZ3r90c/7j7jAMLlwAA+n4/H/Xhwn3Pd51xnzgy+PPd9hqKUUgoAAFhLxbU9AQAANk5CEgCALEISAIAsQhIAgCxCEgCALEISAIAsQhIAgCxCEgCALEISAIAsQhI2MiNHjoyioqIqjxYtWkTv3r3jkUceWe/zGT9+fJW51KlTJ1q1ahXf+c53YtKkSYVxkydPjqKiohg5cuRa72PixIkxZMiQmDx5cs1N/P/317/+NXbbbbdo1KhRFBUVxYMPPrjScSvmv+JRXFwczZo1i759+0ZFRUWNz2t9uuqqq1Z53F/G1KlT44wzzohOnTpFgwYNYosttohu3brFKaecElOnTi2MGzJkSBQVFdX4/oF1T0jCRmrEiBFRUVERzz77bNxyyy1Rp06dOOSQQ+Lhhx+ulflcddVVUVFREePGjYuLL744xo4dG3vttVd8+OGHX3rbEydOjCuuuKLGQzKlFP3794+SkpJ46KGHoqKiInr16rXa15x99tlRUVERTz31VFx99dXx97//PfbZZ5945ZVXanRu69O6CMkPPvggdtlllxg7dmycf/758dhjj8Vvf/vbOOaYY2LChAnx7rvvFsYOGjRoo49x+KqqW9sTAPJ07do1dtttt8Lzgw46KDbffPO4++6745BDDlnv89luu+2iR48eERGx9957x2abbRYnn3xyjBw5Mi699NL1Pp81MW3atPj444/j8MMPj/3222+NXrPVVlsVjnOvvfaKbbfdNvbbb78YNmxYDB8+fKWv+eyzz6J+/fob3FW3zz77LBo0aLBOtj18+PD46KOP4oUXXoiOHTsWlh922GFxySWXRGVlZWFZ27Zto23btutkHsC65YokbCLq168f9erVi5KSkirLP/744zjjjDNiyy23jHr16sXWW28dl156aSxevDgiIhYtWhQ777xzbLvttjFnzpzC62bMmBHl5eXRu3fvWL58+VrPZ0Vsvf/++6sd9/TTT8d+++0XZWVl0bBhw9hzzz3j0UcfLawfOXJkfOc734mIiH322afw1vIXvUX+RdsdMmRIIV4uvvjiKCoqig4dOnzp41zx0YPHH388TjrppGjRokU0bNgwFi9eHJWVlTF06NDo3LlzlJaWRsuWLeOEE06IDz74oMo2e/fuHV27do2nnnoqevToEQ0aNIgtt9wyLrvssmrnYsmSJXHllVcWttmiRYs48cQT49///neVcR06dIh+/frF6NGjY+edd4769evHFVdcEUVFRbFgwYK4/fbbC1/b3r17x+TJk6Nu3bpx9dVXVzvmJ598MoqKiuL3v//9Kr8us2fPjuLi4mjZsuVK1xcX//c/P59/a3tlH9/4v3NbIaUUw4YNi5122ikaNGgQm2++eRx55JFVrnYC65aQhI3U8uXLY9myZbF06dL44IMP4rzzzosFCxbEscceWxizaNGi2GeffeKOO+6I888/Px599NE47rjjYujQoXHEEUdExH8C9L777otZs2bFSSedFBERlZWVMWDAgEgpxd133x116tRZ6/m98847ERHRokWLVY554oknYt999405c+bEbbfdFnfffXeUlZXFIYccEvfee29ERBx88MFx1VVXRUTETTfdFBUVFVFRUREHH3zwl9ruoEGDYvTo0RHx37erH3jggRo7zpNOOilKSkrizjvvjD/84Q9RUlISp59+elx88cVxwAEHxEMPPRQ/+clPYsyYMbHnnnvGRx99VOX1M2bMiKOPPjoGDBgQf/zjH+PII4+MK6+8Ms4999zCmMrKyjj00EPjmmuuiWOPPTYeffTRuOaaa2Ls2LHRu3fv+Oyzz6ps8+WXX46LLroozjnnnBgzZkx8+9vfjoqKimjQoEHhs54VFRUxbNiw6NChQ3zrW9+K3/zmN9Xi9cYbb4w2bdrE4YcfvsqvS8+ePaOysjKOOOKI+POf/xxz585d46/pwQcfXJjLisf1118fERE77LBDYdzgwYPjvPPOi/333z8efPDBGDZsWLzxxhux5557xsyZM9d4f8CXkICNyogRI1JEVHuUlpamYcOGVRn7m9/8JkVEuu+++6osv/baa1NEpMcff7yw7N57700RkW644Yb0ox/9KBUXF1dZvyrjxo1LEZHuvffetHTp0rRw4cL05JNPpm233TbVqVMn/f3vf08ppfTee++liEgjRowovLZHjx6pZcuWad68eYVly5YtS127dk1t27ZNlZWVKaWUfv/736eISOPGjVujr9GabnfFnK677rov3OaKsddee21aunRpWrRoUXrppZfS17/+9RQR6dFHH00p/ff8nHDCCVVeP2nSpBQR6Ywzzqiy/Pnnn08RkS655JLCsl69eqWISH/84x+rjD3llFNScXFxev/991NKKd19990pItL9999fZdyECRNSRFT5fmjfvn2qU6dOeuutt6odW6NGjdLAgQOrLV9xbh944IHCsg8//DDVrVs3XXHFFav5aqVUWVmZBg8enIqLi1NEpKKiotSlS5f0ve99L7333ntVxl5++eVpdf85evPNN1OzZs3SPvvskxYvXpxSSqmioiJFRPr5z39eZezUqVNTgwYN0ve///3Vzg+oGUISNjIrQuWOO+5IEyZMSBMmTEh/+tOf0qmnnpqKiorSr371q8LY/v37p0aNGhXCaYWZM2emiEgXX3xxleWnn356KikpScXFxemHP/zhGs1nRWx8/tGxY8cqAfL5kJw/f34qKiqqFlYp/Td0J02alFJau5Bcm+3mhOTnH61atUo333xzYdyK8/P5CBw2bFiKiPTCCy9U23aXLl3SHnvsUXjeq1evVFZWVm3ciq/1nXfemVJKacCAAWmzzTZLS5YsSUuXLq3yKC8vT/379y+8tn379mnnnXde6bGtKiRTSql79+5p//33Lzy/7LLLUklJSZo+ffpKx3/e5MmT07Bhw9JJJ52Utt122xQRqWHDhmn8+PGFMasLyenTp6cOHTqkrl27pk8//bSw/NJLL01FRUVp5syZ1Y69R48eaffdd1+j+QFfjpttYCPVpUuXajfbvP/++/H9738/jjvuuNhss81i9uzZUV5eXu0mj5YtW0bdunVj9uzZVZafdNJJ8etf/zrq1asX55xzzlrN59prr41999036tSpE82bN4927dqtdvwnn3wSKaVo3bp1tXVt2rSJiKg2vzWxrra7wrnnnhvHHXdcFBcXx2abbRYdO3Zc6U00n9//in2ual6f/yxpq1atqo0rLy+vsq2ZM2fGp59+GvXq1VvpXD//dvnK9v1FzjnnnBg0aFC89dZbsfXWW8fw4cPjyCOPLMzli7Rv3z5OP/30wvP77rsvjjnmmLjooovihRdeWO1r582bF3379o2lS5fGn/70p2jatGlh3cyZMyOltNKvU0TE1ltvvUbzA74cIQmbkB133DH+/Oc/xz//+c/Yfffdo1mzZvH8889HSqlK7MyaNSuWLVsWzZs3LyxbsGBBHH/88dGpU6eYOXNmDBo0KP74xz+u8b633nrrKmH7RTbffPMoLi6O6dOnV1s3bdq0iIgq86vt7a7Qtm3bNTrOz8dls2bNIiJi+vTp1e5QnjZtWrU5rewzfjNmzKiyrebNm0ezZs1izJgxK51DWVnZaue0Jo499ti4+OKL46abbooePXrEjBkz4swzz1zr7azQv3//uPrqq+P1119f7bilS5fGt7/97fjXv/4VTz31VLWvWfPmzaOoqCieeuqpKC0trfb6lS0Dap6bbWAT8uqrr0bEf2/82G+//WL+/PnVfkfgHXfcUVi/wmmnnRZTpkyJ0aNHx2233RYPPfRQ/OIXv1hnc23UqFHsscceMXr06Co3hVRWVsZdd90Vbdu2jU6dOkXEf6Pg8zePfNntrk/77rtvRETcddddVZZPmDAhJk2aVO3XD82bNy8eeuihKst+97vfRXFxcey9994REdGvX7+YPXt2LF++PHbbbbdqj+23336N5lZaWrrKr239+vXj1FNPjdtvvz2uv/762GmnnWKvvfb6wm2uLOQjIubPnx9Tp04tXB1elZNPPjnGjx8fo0ePjh133LHa+n79+kVKKT788MOVHnu3bt2+cI7Al+eKJGykXn/99Vi2bFlE/OetztGjR8fYsWPj8MMPL/zevhNOOCFuuummGDhwYEyePDm6desWTz/9dFx11VXRt2/f2H///SMi4tZbb4277rorRowYETvssEPssMMOcdZZZ8XFF18ce+21V+y+++7r5BiuvvrqOOCAA2KfffaJCy+8MOrVqxfDhg2L119/Pe6+++7CFbSuXbtGRMQtt9wSZWVlUb9+/ejYsWPhylzudten7bffPk499dT41a9+FcXFxdGnT5+YPHlyXHbZZdGuXbv43ve+V2V8s2bN4vTTT48pU6ZEp06d4rHHHovhw4fH6aefHltttVVERBx99NExatSo6Nu3b5x77rmx++67R0lJSXzwwQcxbty4OPTQQ1d7Z/UK3bp1i/Hjx8fDDz8crVu3jrKysioResYZZ8TQoUPjpZdeiltvvXWNjvenP/1pPPPMM3HUUUcVfj3Pe++9FzfeeGPMnj07rrvuulW+9rrrros777wzzj777GjUqFE899xzhXVNmjSJr33ta7HXXnvFqaeeGieeeGK8+OKLsffee0ejRo1i+vTp8fTTT0e3bt2qvKUOrCO1+glNYK2t7K7tpk2bpp122ildf/31adGiRVXGz549O5122mmpdevWqW7duql9+/bpBz/4QWHca6+9lho0aFDtZotFixalXXfdNXXo0CF98sknq5zPihtAfv/736923iu7azullJ566qm07777pkaNGqUGDRqkHj16pIcffrja62+44YbUsWPHVKdOnZVu5/PWZLs5N9t80dgV52fChAnV1i1fvjxde+21qVOnTqmkpCQ1b948HXfccWnq1KlVxvXq1SvtsMMOafz48Wm33XZLpaWlqXXr1umSSy5JS5curTJ26dKl6Wc/+1nq3r17ql+/fmrcuHHq3LlzGjx4cHr77bcL49q3b58OPvjglc751VdfTXvttVdq2LBhiojUq1evamN69+6dtthii7Rw4cLVHv8Kzz33XDrzzDNT9+7d0xZbbJHq1KmTWrRokQ466KD02GOPVRn7+ZttBg4cuNIbm1Y2t9/+9rdpjz32KJznbbbZJp1wwgnpxRdfXKN5Al9OUUopre94BWDVevfuHR999NEXfo5wfZk1a1a0b98+zj777Bg6dGhtTwfYgHhrG4CV+uCDD+Ldd9+N6667LoqLi6v8MnSACDfbALAKt956a/Tu3TveeOONGDVqVGy55Za1PSVgA+OtbQAAsrgiCQBAFiEJAEAWIQkAQJb1ftd2ZWVlTJs2LcrKymrllwIDALB6KaWYN29etGnTJoqLV33dcb2H5LRp06Jdu3bre7cAAKylqVOnVvu37v+v9R6SZWVlEfGfiTVp0mR97x4AgC8wd+7caNeuXaHbVmW9h+SKt7ObNGkiJAEANmBf9DFEN9sAAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQpW5tTwBYc2+//XbMmzevtqexSStatijqz58SixpvFalu/dqeTo0qKyuL7bbbrranAWxChCRsJN5+++3o1KlTbU9jk7dzeXG8PLhx7HLz/HhlRmVtT6fG/fOf/xSTQI0RkrCRWHEl8q677oou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LEISAIAsQhIAgCxCEgCALEISAIAsQhIAgCxCEgCALEISAIAsQhIAgCxCEgCALEISAIAsQhIAgCxCEgCALEISAIAsQhIAgCxCEgCALEISAIAsQhIAgCxCEgCALEISAIAsQhIAgCxCEgCALEISAIAsQhIAgCxCEgCALEISAIAsQhIAgCxCEgCALEISAIAsQhIAgCxCEgCALEISAIAsQhIAgCxCEgCALEISAIAsQhIAgCxCEgCALEISAIAsQhIAgCxCEgCALEISAIAsQhIAgCxCEgCALEISAIAsQhIAgCxCEgCALEISAIAsQhIAgCxCEgCALEISAIAsQhIAgCxCEgCALEISAIAsQhIAgCxCEgCALEISAIAsQhIAgCxCEgCALEISAIAsQhIAgCxCEgCALEISAIAsQhIAgCxCEgCALEISAIAsQhIAgCxCEgCALEISAIAsQhIAgCxCEgCALEISAIAsQhIAgCxCEgCALEISAIAsQhIAgCxCEgCALEISAIAsQhIAgCxCEgCALEISAIAsQhIAgCxCEgCALEISAIAsQhIAgCxCEgCALEISAIAsQhIAgCxCEgCALEISAIAsQhIAgCxCEgCALEISAIAsQhIAgCxCEgCALEISAIAsQhIAgCxCEgCALEISAIAsQhIAgCxCEgCALEISAIAsQhIAgCxCEgCALEISAIAsQhIAgCxCEgCALEISAIAsQhIAgCxCEgCALEISAIAsQhIAgCxCEgCALEISAIAsQhIAgCxCEgCALEISAIAsQhIAgCxCEgCALEISAIAsQhIAgCxCEgCALEISAIAsQhIAgCxCEgCALEISAIAsQhIAgCxCEgCALEISAIAsQhIAgCxCEgCALEISAIAsQhIAgCxCEgCALEISAIAsQhIAgCxCEgCALEISAIAsQhIAgCxCEgCALEISAIAsQhIAgCxCEgCALEISAIAsQhIAgCxCEgCALEISAIAsQhIAgCxCEgCALEISAIAsQhIAgCxCEgCALEISAIAsQhIAgCxCEgCALEISAIAsQhIAgCxCEgCALEISAIAsQhIAgCxCEgCALEISAIAsQhIAgCx11/cOU0oRETF37tz1vWsAANbAik5b0W2rst5Dct68eRER0a5du/W9awAA1sK8efOiadOmq1xflL4oNWtYZWVlTJs2LcrKyqKoqGid72/u3LnRrl27mDp1ajRp0mSd748Ni/P/1eb8f7U5/19tzv+Xk1KKefPmRZs2baK4eNWfhFzvVySLi4ujbdu263u30aRJE99IX2HO/1eb8//V5vx/tTn/+VZ3JXIFN9sAAJBFSAIAkGWTD8nS0tK4/PLLo7S0tLanQi1w/r/anP+vNuf/q835Xz/W+802AABsGjb5K5IAAKwbQhIAgCxCEgCALEISAIAsm3RIDhs2LDp27Bj169ePXXfdNZ566qnanhJf0pAhQ6KoqKjKo7y8vLA+pRRDhgyJNm3aRIMGDaJ3797xxhtvVNnG4sWL4+yzz47mzZtHo0aN4lvf+lZ88MEH6/tQWENPPvlkHHLIIdGmTZsoKiqKBx98sMr6mjrnn3zySRx//PHRtGnTaNq0aRx//PHx6aefruOj44t80fn/7ne/W+3vhB49elQZ4/xvnK6++ur4+te/HmVlZdGyZcs47LDD4q233qoyxs9/7dtkQ/Lee++N8847Ly699NJ45ZVX4v/9v/8Xffr0iSlTptT21PiSdthhh5g+fXrh8Y9//KOwbujQoXH99dfHjTfeGBMmTIjy8vI44IADCv/Ge0TEeeedFw888EDcc8898fTTT8f8+fOjX79+sXz58to4HL7AggULonv37nHjjTeudH1NnfNjjz02Xn311RgzZkyMGTMmXn311Tj++OPX+fGxel90/iMiDjrooCp/Jzz22GNV1jv/G6cnnngizjzzzHjuuedi7NixsWzZsjjwwANjwYIFhTF+/jcAaRO1++67p9NOO63Kss6dO6f/+Z//qaUZURMuv/zy1L1795Wuq6ysTOXl5emaa64pLFu0aFFq2rRp+s1vfpNSSunTTz9NJSUl6Z577imM+fDDD1NxcXEaM2bMOp07X15EpAceeKDwvKbO+cSJE1NEpOeee64wpqKiIkVEevPNN9fxUbGmPn/+U0pp4MCB6dBDD13la5z/TcesWbNSRKQnnngipeTnf0OxSV6RXLJkSbz00ktx4IEHVll+4IEHxrPPPltLs6KmvP3229GmTZvo2LFjHH300fHuu+9GRMR7770XM2bMqHLeS0tLo1evXoXz/tJLL8XSpUurjGnTpk107drV98ZGqKbOeUVFRTRt2jT22GOPwpgePXpE06ZNfV9sBMaPHx8tW7aMTp06xSmnnBKzZs0qrHP+Nx1z5syJiIgtttgiIvz8byg2yZD86KOPYvny5dGqVasqy1u1ahUzZsyopVlRE/bYY4+444474s9//nMMHz48ZsyYEXvuuWfMnj27cG5Xd95nzJgR9erVi80333yVY9h41NQ5nzFjRrRs2bLa9lu2bOn7YgPXp0+fGDVqVPztb3+Ln//85zFhwoTYd999Y/HixRHh/G8qUkpx/vnnxze+8Y3o2rVrRPj531DUre0JrEtFRUVVnqeUqi1j49KnT5/Cn7t16xY9e/aMbbbZJm6//fbCB+xzzrvvjY1bTZzzlY33fbHhO+qoowp/7tq1a+y2227Rvn37ePTRR+OII45Y5euc/43LWWedFa+99lo8/fTT1db5+a9dm+QVyebNm0edOnWq/Z/ErFmzqv2fCxu3Ro0aRbdu3eLtt98u3L29uvNeXl4eS5YsiU8++WSVY9h41NQ5Ly8vj5kzZ1bb/r///W/fFxuZ1q1bR/v27ePtt9+OCOd/U3D22WfHQw89FOPGjYu2bdsWlvv53zBskiFZr1692HXXXWPs2LFVlo8dOzb23HPPWpoV68LixYtj0qRJ0bp16+jYsWOUl5dXOe9LliyJJ554onDed9111ygpKakyZvr06fH666/73tgI1dQ579mzZ8yZMydeeOGFwpjnn38+5syZ4/tiIzN79uyYOnVqtG7dOiKc/41ZSinOOuusGD16dPztb3+Ljh07Vlnv538DUSu3+KwH99xzTyopKUm33XZbmjhxYjrvvPNSo0aN0uTJk2t7anwJF1xwQRo/fnx6991303PPPZf69euXysrKCuf1mmuuSU2bNk2jR49O//jHP9IxxxyTWrdunebOnVvYxmmnnZbatm2b/vKXv6SXX3457bvvvql79+5p2bJltXVYrMa8efPSK6+8kl555ZUUEen6669Pr7zySnr//fdTSjV3zg866KC04447poqKilRRUZG6deuW+vXrt96Pl6pWd/7nzZuXLrjggvTss8+m9957L40bNy717Nkzbbnlls7/JuD0009PTZs2TePHj0/Tp08vPBYuXFgY4+e/9m2yIZlSSjfddFNq3759qlevXtpll10KvzKAjddRRx2VWrdunUpKSlKbNm3SEUcckd54443C+srKynT55Zen8vLyVFpamvbee+/0j3/8o8o2Pvvss3TWWWelLbbYIjVo0CD169cvTZkyZX0fCmto3LhxKSKqPQYOHJhSqrlzPnv27DRgwIBUVlaWysrK0oABA9Inn3yyno6SVVnd+V+4cGE68MADU4sWLVJJSUnaaqut0sCBA6udW+d/47Sy8x4RacSIEYUxfv5rX1FKKa3vq6AAAGz8NsnPSAIAsO4JSQAAsghJAACyCEkAALIISQAAsghJAACyCEkAALIISQAAsghJgI3MkCFDYqeddqrtaQAISWDD893vfjeKioqiqKgoSkpKYuutt44LL7wwFixYUNtTW6WRI0fGZpttViPbuv/++2OPPfaIpk2bRllZWeywww5xwQUXFNZfeOGF8de//rVG9gXwZdSt7QkArMxBBx0UI0aMiKVLl8ZTTz0VgwYNigULFsSvf/3ramOXLl0aJSUltTDL/+6/pvzlL3+Jo48+Oq666qr41re+FUVFRTFx4sQq4di4ceNo3Lhxje0TIJcrksAGqbS0NMrLy6Ndu3Zx7LHHxoABA+LBBx+MiP++tfvb3/42tt566ygtLY2UUkyZMiUOPfTQaNy4cTRp0iT69+8fM2fOLGxzxetuvvnmaNeuXTRs2DC+853vxKefflpl3yNGjIguXbpE/fr1o3PnzjFs2LDCusmTJ0dRUVHcd9990bt376hfv37cddddceKJJ8acOXMKV1KHDBkSP/7xj6Nbt27Vjm3XXXeNH/3oRys97kceeSS+8Y1vxEUXXRTbb799dOrUKQ477LD41a9+Ve04Vlixz//76NChQ2H9xIkTo2/fvtG4ceNo1apVHH/88fHRRx+txdkAWDkhCWwUGjRoUOXK3zvvvBP33Xdf3H///fHqq69GRMRhhx0WH3/8cTzxxBMxduzY+Ne//hVHHXVUle2seN3DDz8cY8aMiVdffTXOPPPMwvrhw4fHpZdeGj/96U9j0qRJcdVVV8Vll10Wt99+e5XtXHzxxXHOOefEpEmTYr/99osbbrghmjRpEtOnT4/p06fHhRdeGCeddFJMnDgxJkyYUHjda6+9Fq+88kp897vfXelxlpeXxxtvvBGvv/76Gn9tVuxz+vTp8c4778S2224be++9d2Fdr169YqeddooXX3wxxowZEzNnzoz+/fuv8fYBVikBbGAGDhyYDj300MLz559/PjVr1iz1798/pZTS5ZdfnkpKStKsWbMKYx5//PFUp06dNGXKlMKyN954I0VEeuGFFwqvq1OnTpo6dWphzJ/+9KdUXFycpk+fnlJKqV27dul3v/tdlfn85Cc/ST179kwppfTee++liEg33HBDlTEjRoxITZs2rXYsffr0Saeffnrh+XnnnZd69+69ymOfP39+6tu3b4qI1L59+3TUUUel2267LS1atKgw5vLLL0/du3ev9trKysp0+OGHp1133TUtXLgwpZTSZZddlg488MAq46ZOnZoiIr311lurnAfAmnBFEtggPfLII9G4ceOoX79+9OzZM/bee+8qb++2b98+WrRoUXg+adKkaNeuXbRr166w7Gtf+1psttlmMWnSpMKyrbbaKtq2bVt43rNnz6isrIy33nor/v3vf8fUqVPj5JNPLnwOsXHjxnHllVfGv/71ryrz22233dboOE455ZS4++67Y9GiRbF06dIYNWpUnHTSSasc36hRo3j00UfjnXfeiR/+8IfRuHHjuOCCC2L33XePhQsXrnZfl1xySVRUVMSDDz4YDRo0iIiIl156KcaNG1fleDp37hwRUe2YANaWm22ADdI+++wTv/71r6OkpCTatGlT7WaaRo0aVXmeUoqioqJq21nV8hVWrCsqKorKysqI+M/b23vssUeVcXXq1Fnt/lflkEMOidLS0njggQeitLQ0Fi9eHN/+9re/8HXbbLNNbLPNNjFo0KC49NJLo1OnTnHvvffGiSeeuNLxd911V/ziF7+I8ePHVwnlysrKOOSQQ+Laa6+t9prWrVuv0TEArIqQBDZIjRo1im233XaNx3/ta1+LKVOmxNSpUwtXJSdOnBhz5syJLl26FMZNmTIlpk2bFm3atImIiIqKiiguLo5OnTpFq1atYsstt4x33303BgwYsFbzrVevXixfvrza8rp168bAgQNjxIgRUVpaGkcffXQ0bNhwrbbdoUOHaNiw4Sp//VFFRUUMGjQobr755ujRo0eVdbvsskvcf//90aFDh6hb11/5QM3ytwqwSdh///1jxx13jAEDBsQNN9wQy5YtizPOOCN69epV5W3o+vXrx8CBA+NnP/tZzJ07N84555zo379/lJeXR8R/7og+55xzokmTJtGnT59YvHhxvPjii/HJJ5/E+eefv8r9d+jQIebPnx9//etfo3v37tGwYcNCMA4aNKgQs88888xqj2PIkCGxcOHC6Nu3b7Rv3z4+/fTT+OUvfxlLly6NAw44oNr4GTNmxOGHHx5HH310fPOb34wZM2ZExH+uoLZo0SLOPPPMGD58eBxzzDFx0UUXRfPmzeOdd96Je+65J4YPH17tSivA2vAZSWCTUFRUFA8++GBsvvnmsffee8f+++8fW2+9ddx7771Vxm277bZxxBFHRN++fePAAw+Mrl27Vvn1PoMGDYpbb701Ro4cGd26dYtevXrFyJEjo2PHjqvd/5577hmnnXZaHHXUUdGiRYsYOnRoYd12220Xe+65Z2y//fbV3jL/vF69esW7774bJ5xwQnTu3Dn69OkTM2bMiMcffzy23377auPffPPNmDlzZtx+++3RunXrwuPrX/96RES0adMmnnnmmVi+fHl885vfjK5du8a5554bTZs2jeJi/wkAvpyilFKq7UkArA9DhgyJBx98sPDrgtaXlFJ07tw5Bg8evNqrmgAbG29tA6xDs2bNijvvvDM+/PDDVd4oA7CxEpIA61CrVq2iefPmccstt8Tmm29e29MBqFHe2gYAIItPWgMAkEVIAgCQRUgCAJBFSAIAkEVIAgCQRUgCAJBFSAIAkEVIAgCQ5f8DJRV7KQth1u4AAAAASUVORK5CYII=",
      "text/plain": [
       "<Figure size 800x600 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Create a box plot\n",
    "plt.figure(figsize=(8, 6))\n",
    "plt.boxplot(df['property_size'], vert=False)\n",
    "plt.title('Box Plot of Property Size')\n",
    "plt.xlabel('Property Size')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2.0     9921\n",
       "1.0     5381\n",
       "3.0     2224\n",
       "4.0      135\n",
       "5.0        5\n",
       "21.0       1\n",
       "Name: bathroom, dtype: int64"
      ]
     },
     "execution_count": 78,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['bathroom'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAApIAAAIhCAYAAAD91lq9AAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/YYfK9AAAACXBIWXMAAA9hAAAPYQGoP6dpAAAwSklEQVR4nO3dd5xU5b348e8unZWigAJSlQgoWFFBVECNDQ3EKBprNJbYjSZiLD/xxiiWmKISExuWXK5RkRixQG5AUUFR0ViQoIJgBIxEAUEQ4fn94d2JC7sLPLJLe79fr33pnHnOOc+cPa/ZjzNzxqKUUgoAAFhDxet6AgAAbJiEJAAAWYQkAABZhCQAAFmEJAAAWYQkAABZhCQAAFmEJAAAWYQkAABZhCRsYIYOHRpFRUVlfpo1axa9e/eOxx57rNrnM3bs2DJzqVGjRmy11VZx1FFHxeTJkwvjpk+fHkVFRTF06NA13sdbb70VgwYNiunTp6+9if+f//3f/41u3bpFSUlJFBUVxYgRI8odVzr/0p/i4uJo0qRJHHrooTF+/Pi1Pq/qdM0111T4uL+JmTNnxllnnRXbbbdd1KtXL7bYYovo2rVrnHbaaTFz5szCuEGDBkVRUdFa3z9Q9YQkbKDuvvvuGD9+fDz//PPxhz/8IWrUqBGHH354/OUvf1kn87nmmmti/PjxMWbMmBg4cGCMHj06evbsGf/85z+/8bbfeuutuOqqq9Z6SKaUYsCAAVGrVq149NFHY/z48dGrV69K1zn33HNj/PjxMW7cuLj22mvjtddeiz59+sSkSZPW6tyqU1WE5AcffBC77rprjB49Oi688MJ4/PHH46677orvf//7MXHixHjvvfcKY0899dQNPsZhU1VzXU8AyNOlS5fo1q1b4fbBBx8cm2++eQwbNiwOP/zwap/Pt771rejevXtEROy7777RuHHj+OEPfxhDhw6Nyy67rNrnszo+/PDD+Pe//x3f/e53Y//991+tddq0aVN4nD179owOHTrE/vvvH0OGDInbb7+93HU+//zzqFu37nr3qtvnn38e9erVq5Jt33777fHxxx/Hiy++GO3bty8s79+/f1x66aWxfPnywrJWrVpFq1atqmQeQNXyiiRsJOrWrRu1a9eOWrVqlVn+73//O84666zYeuuto3bt2rHNNtvEZZddFkuWLImIiMWLF8cuu+wSHTp0iHnz5hXWmz17djRv3jx69+4dy5YtW+P5lMbW+++/X+m4Z599Nvbff/9o0KBB1K9fP/baa68YOXJk4f6hQ4fGUUcdFRERffr0Kby1vKq3yFe13UGDBhXiZeDAgVFUVBTt2rX7xo+z9KMHo0aNilNOOSWaNWsW9evXjyVLlsTy5cvj+uuvj06dOkWdOnViyy23jBNPPDE++OCDMtvs3bt3dOnSJcaNGxfdu3ePevXqxdZbbx1XXHHFSr+LL774Iq6++urCNps1axYnn3xy/Otf/yozrl27dnHYYYfF8OHDY5dddom6devGVVddFUVFRbFw4cK45557Cse2d+/eMX369KhZs2Zce+21Kz3mZ555JoqKiuLBBx+s8LjMnTs3iouLY8sttyz3/uLi//z5WfGt7fI+vvH1uZVKKcWQIUNi5513jnr16sXmm28eRx55ZJlXO4GqJSRhA7Vs2bL48ssvY+nSpfHBBx/EBRdcEAsXLoxjjz22MGbx4sXRp0+fuPfee+PCCy+MkSNHxvHHHx/XX399HHHEERHxVYD+6U9/io8++ihOOeWUiIhYvnx5HHfccZFSimHDhkWNGjXWeH7vvPNOREQ0a9aswjFPP/107LfffjFv3ry48847Y9iwYdGgQYM4/PDD44EHHoiIiL59+8Y111wTERG33nprjB8/PsaPHx99+/b9Rts99dRTY/jw4RHxn7erH3nkkbX2OE855ZSoVatW3HffffHQQw9FrVq14swzz4yBAwfGt7/97Xj00Ufj5z//eTz55JOx1157xccff1xm/dmzZ8cxxxwTxx13XPz5z3+OI488Mq6++uo4//zzC2OWL18e/fr1i8GDB8exxx4bI0eOjMGDB8fo0aOjd+/e8fnnn5fZ5iuvvBI//elP47zzzosnn3wyvve978X48eOjXr16hc96jh8/PoYMGRLt2rWL73znO3HbbbetFK+33HJLtGzZMr773e9WeFx69OgRy5cvjyOOOCKeeuqpmD9//mof0759+xbmUvpz0003RUTEDjvsUBh3xhlnxAUXXBAHHHBAjBgxIoYMGRJvvvlm7LXXXjFnzpzV3h/wDSRgg3L33XeniFjpp06dOmnIkCFlxt52220pItKf/vSnMsuvu+66FBFp1KhRhWUPPPBAioj061//Ov2///f/UnFxcZn7KzJmzJgUEemBBx5IS5cuTYsWLUrPPPNM6tChQ6pRo0Z67bXXUkopTZs2LUVEuvvuuwvrdu/ePW255ZZpwYIFhWVffvll6tKlS2rVqlVavnx5SimlBx98MEVEGjNmzGodo9XdbumcbrjhhlVus3Tsddddl5YuXZoWL16cXn755bT77runiEgjR45MKf3n93PiiSeWWX/y5MkpItJZZ51VZvkLL7yQIiJdeumlhWW9evVKEZH+/Oc/lxl72mmnpeLi4vT++++nlFIaNmxYioj08MMPlxk3ceLEFBFlzoe2bdumGjVqpClTpqz02EpKStJJJ5200vLS3+0jjzxSWPbPf/4z1axZM1111VWVHK2Uli9fns4444xUXFycIiIVFRWlzp07px//+Mdp2rRpZcZeeeWVqbI/R2+//XZq0qRJ6tOnT1qyZElKKaXx48eniEi//OUvy4ydOXNmqlevXrr44osrnR+wdghJ2MCUhsq9996bJk6cmCZOnJieeOKJdPrpp6eioqJ08803F8YOGDAglZSUFMKp1Jw5c1JEpIEDB5ZZfuaZZ6ZatWql4uLidPnll6/WfEpjY8Wf9u3blwmQFUPys88+S0VFRSuFVUr/Cd3JkyenlNYsJNdkuzkhueLPVlttlX7/+98XxpX+flaMwCFDhqSISC+++OJK2+7cuXPac889C7d79eqVGjRosNK40mN93333pZRSOu6441Ljxo3TF198kZYuXVrmp3nz5mnAgAGFddu2bZt22WWXch9bRSGZUko77bRTOuCAAwq3r7jiilSrVq00a9ascsevaPr06WnIkCHplFNOSR06dEgRkerXr5/Gjh1bGFNZSM6aNSu1a9cudenSJX366aeF5ZdddlkqKipKc+bMWemxd+/ePe2xxx6rNT/gm3GxDWygOnfuvNLFNu+//35cfPHFcfzxx0fjxo1j7ty50bx585Uu8thyyy2jZs2aMXfu3DLLTznllPjd734XtWvXjvPOO2+N5nPdddfFfvvtFzVq1IimTZtG69atKx3/ySefREopWrRosdJ9LVu2jIhYaX6ro6q2W+r888+P448/PoqLi6Nx48bRvn37ci+iWXH/pfusaF4rfpZ0q622Wmlc8+bNy2xrzpw58emnn0bt2rXLneuKb5eXt+9VOe+88+LUU0+NKVOmxDbbbBO33357HHnkkYW5rErbtm3jzDPPLNz+05/+FN///vfjpz/9abz44ouVrrtgwYI49NBDY+nSpfHEE09Eo0aNCvfNmTMnUkrlHqeIiG222Wa15gd8M0ISNiI77rhjPPXUU/GPf/wj9thjj2jSpEm88MILkVIqEzsfffRRfPnll9G0adPCsoULF8YJJ5wQ2223XcyZMydOPfXU+POf/7za+95mm23KhO2qbL755lFcXByzZs1a6b4PP/wwIqLM/Nb1dku1atVqtR7ninHZpEmTiIiYNWvWSlcof/jhhyvNqbzP+M2ePbvMtpo2bRpNmjSJJ598stw5NGjQoNI5rY5jjz02Bg4cGLfeemt07949Zs+eHWefffYab6fUgAED4tprr4033nij0nFLly6N733ve/Huu+/GuHHjVjpmTZs2jaKiohg3blzUqVNnpfXLWwasfS62gY3Iq6++GhH/ufBj//33j88++2yl7wi89957C/eX+tGPfhQzZsyI4cOHx5133hmPPvpo/OpXv6qyuZaUlMSee+4Zw4cPL3NRyPLly+P++++PVq1axXbbbRcR/4mCFS8e+abbrU777bdfRETcf//9ZZZPnDgxJk+evNLXDy1YsCAeffTRMsv++7//O4qLi2PfffeNiIjDDjss5s6dG8uWLYtu3bqt9NOxY8fVmludOnUqPLZ169aN008/Pe6555646aabYuedd46ePXuucpvlhXxExGeffRYzZ84svDpckR/+8IcxduzYGD58eOy4444r3X/YYYdFSin++c9/lvvYu3btuso5At+cVyRhA/XGG2/El19+GRFfvdU5fPjwGD16dHz3u98tfG/fiSeeGLfeemucdNJJMX369OjatWs8++yzcc0118Shhx4aBxxwQERE3HHHHXH//ffH3XffHTvssEPssMMOcc4558TAgQOjZ8+esccee1TJY7j22mvj29/+dvTp0yd+8pOfRO3atWPIkCHxxhtvxLBhwwqvoHXp0iUiIv7whz9EgwYNom7dutG+ffvCK3O5261OHTt2jNNPPz1uvvnmKC4ujkMOOSSmT58eV1xxRbRu3Tp+/OMflxnfpEmTOPPMM2PGjBmx3XbbxeOPPx633357nHnmmdGmTZuIiDjmmGPij3/8Yxx66KFx/vnnxx577BG1atWKDz74IMaMGRP9+vWr9MrqUl27do2xY8fGX/7yl2jRokU0aNCgTISeddZZcf3118fLL78cd9xxx2o93l/84hfx3HPPxdFHH134ep5p06bFLbfcEnPnzo0bbrihwnVvuOGGuO++++Lcc8+NkpKSmDBhQuG+hg0bxvbbbx89e/aM008/PU4++eR46aWXYt99942SkpKYNWtWPPvss9G1a9cyb6kDVWSdfkITWGPlXbXdqFGjtPPOO6ebbropLV68uMz4uXPnph/96EepRYsWqWbNmqlt27bpZz/7WWHc3//+91SvXr2VLrZYvHhx2m233VK7du3SJ598UuF8Si8AefDBByudd3lXbaeU0rhx49J+++2XSkpKUr169VL37t3TX/7yl5XW//Wvf53at2+fatSoUe52VrQ628252GZVY0t/PxMnTlzpvmXLlqXrrrsubbfddqlWrVqpadOm6fjjj08zZ84sM65Xr15phx12SGPHjk3dunVLderUSS1atEiXXnppWrp0aZmxS5cuTTfeeGPaaaedUt26ddNmm22WOnXqlM4444w0derUwri2bdumvn37ljvnV199NfXs2TPVr18/RUTq1avXSmN69+6dtthii7Ro0aJKH3+pCRMmpLPPPjvttNNOaYsttkg1atRIzZo1SwcffHB6/PHHy4xd8WKbk046qdwLm8qb21133ZX23HPPwu952223TSeeeGJ66aWXVmuewDdTlFJK1R2vAFSsd+/e8fHHH6/yc4TV5aOPPoq2bdvGueeeG9dff/26ng6wHvHWNgDl+uCDD+K9996LG264IYqLi8t8GTpAhIttAKjAHXfcEb17944333wz/vjHP8bWW2+9rqcErGe8tQ0AQBavSAIAkEVIAgCQRUgCAJCl2q/aXr58eXz44YfRoEGDdfKlwAAAVC6lFAsWLIiWLVtGcXHFrztWe0h++OGH0bp16+reLQAAa2jmzJkr/b/uv67aQ7JBgwYR8dXEGjZsWN27BwBgFebPnx+tW7cudFtFqj0kS9/ObtiwoZAEAFiPrepjiC62AQAgi5AEACCLkAQAIIuQBAAgi5AEACCLkAQAIIuQBAAgi5AEACCLkAQAIIuQBAAgi5AEACCLkAQAIIuQBAAgi5AEACCLkAQAIIuQBAAgi5AEACCLkAQAIIuQBAAgi5AEACCLkAQAIIuQBAAgi5AEACCLkAQAIIuQBAAgi5AEACCLkAQAIIuQBAAgi5AEACCLkAQAIIuQBAAgi5AE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JAEAyCIkAQDIIiQBAMgiJAEAyCIkAQDIIiQBAMgiJAEAyCIkAQDIIiQBAMgiJAEAyCIkAQDIIiQBAMgiJAEAyCIkAQDIIiQBAMgiJAEAyCIkAQDIIiQBAMgiJAEAyCIkAQDIIiQBAMgiJAEAyCIkAQDIIiQBAMgiJAEAyCIkAQDIIiQBAMgiJAEAyCIkAQDIIiQBAMgiJAEAyCIkAQDIIiQBAMgiJAEAyCIkAQDIIiQBAMgiJAEAyCIkAQDIIiQBAMgiJAEAyCIkAQDIIiQBAMgiJAEAyCIkAQDIIiQBAMgiJAEAyCIkAQDIIiQBAMgiJAEAyCIkAQDIIiQBAMgiJAEAyCIkAQDIIiQBAMgiJAEAyCIkAQDIIiQBAMgiJAEAyCIkAQDIIiQBAMgiJAEAyCIkAQDIIiQBAMgiJAEAyCIkAQDIIiQBAMgiJAEAyCIkAQDIIiQBAMgiJAEAyCIkAQDIIiQBAMgiJAEAyCIkAQDIIiQBAMgiJAEAyCIkAQDIIiQBAMgiJAEAyCIkAQDIIiQBAMgiJAEAyCIkAQDIIiQBAMgiJAEAyCIkAQDIIiQBAMgiJAEAyCIkAQDIIiQBAMgiJAEAyCIkAQDIIiQBAMgiJAEAyCIkAQDIIiQBAMgiJAEAyCIkAQDIIiQBAMgiJAEAyCIkAQDIIiQBAMgiJAEAyCIkAQDIIiQBAMgiJAEAyCIkAQDIIiQBAMgiJAEAyCIkAQDIIiQBAMgiJAEAyCIkAQDIIiQBAMgiJAEAyCIkAQDIIiQBAMgiJAEAyCIkAQDIIiQBAMgiJAEAyCIkAQDIIiQBAMgiJAEAyCIkAQDIIiQBAMgiJAEAyCIkAQDIIiQBAMgiJAEAyCIkAQDIIiQBAMgiJAEAyCIkAQDIIiQBAMgiJAEAyCIkAQDIIiQBAMgiJAEAyCIkAQDIIiQBAMgiJAEAyCIkAQDIIiQBAMgiJAEAyCIkAQDIIiQBAMgiJAEAyCIkAQDIIiQBAMgiJAEAyCIkAQDIIiQBAMgiJAEAyCIkAQDIIiQBAMgiJAEAyCIkAQDIIiQBAMgiJAEAyCIkAQDIIiQBAMgiJAEAyCIkAQDIIiQBAMgiJAEAyCIkAQDIIiQBAMgiJAEAyCIkAQDIIiQBAMgiJAEAyCIkAQDIIiQBAMgiJAEAyCIkAQDIIiQBAMgiJAEAyCIkAQDIIiQBAMgiJAEAyCIkAQDIUrO6d5hSioiI+fPnV/euAQBYDaWdVtptFan2kJw7d25ERLRu3bq6dw0AwBpYsGBBNGrUqML7qz0kt9hii4iImDFjRqUT29TMnz8/WrduHTNnzoyGDRuu6+msVxyb8jku5XNcKubYlM9xqZhjU75N4biklGLBggXRsmXLSsdVe0gWF3/1scxGjRpttAf/m2jYsKHjUgHHpnyOS/kcl4o5NuVzXCrm2JRvYz8uq/OCn4ttAADIIiQBAMhS7SFZp06duPLKK6NOnTrVvev1muNSMcemfI5L+RyXijk25XNcKubYlM9x+Y+itKrrugEAoBze2gYAIIuQBAAgi5AEACCLkAQAIMtaD8khQ4ZE+/bto27durHbbrvFuHHjKh3/9NNPx2677RZ169aNbbbZJm677ba1PaV17tprr43dd989GjRoEFtuuWX0798/pkyZUuk6Y8eOjaKiopV+3n777WqadfUYNGjQSo+xefPmla6zKZwz7dq1K/f3f/bZZ5c7fmM9X5555pk4/PDDo2XLllFUVBQjRowoc39KKQYNGhQtW7aMevXqRe/evePNN99c5XYffvjh2H777aNOnTqx/fbbxyOPPFJFj6DqVHZsli5dGgMHDoyuXbtGSUlJtGzZMk488cT48MMPK93m0KFDyz2PFi9eXMWPZu1Z1Tnzgx/8YKXH171791Vud2M/ZyKi3N99UVFR3HDDDRVuc2M4Z1bnb/Sm/FyzKms1JB944IG44IIL4rLLLotJkybFPvvsE4ccckjMmDGj3PHTpk2LQw89NPbZZ5+YNGlSXHrppXHeeefFww8/vDantc49/fTTcfbZZ8eECRNi9OjR8eWXX8aBBx4YCxcuXOW6U6ZMiVmzZhV+vvWtb1XDjKvXDjvsUOYxvv766xWO3VTOmYkTJ5Y5JqNHj46IiKOOOqrS9Ta282XhwoWx0047xS233FLu/ddff33cdNNNccstt8TEiROjefPm8e1vfzsWLFhQ4TbHjx8fRx99dJxwwgnx2muvxQknnBADBgyIF154oaoeRpWo7NgsWrQoXnnllbjiiivilVdeieHDh8c//vGP+M53vrPK7TZs2LDMOTRr1qyoW7duVTyEKrGqcyYi4uCDDy7z+B5//PFKt7kpnDMRsdLv/a677oqioqL43ve+V+l2N/RzZnX+Rm/KzzWrlNaiPfbYI/3oRz8qs6xTp07pkksuKXf8xRdfnDp16lRm2RlnnJG6d+++Nqe13vnoo49SRKSnn366wjFjxoxJEZE++eST6pvYOnDllVemnXbaabXHb6rnzPnnn5+23XbbtHz58nLv3xTOl4hIjzzySOH28uXLU/PmzdPgwYMLyxYvXpwaNWqUbrvttgq3M2DAgHTwwQeXWXbQQQelY445Zq3PubqseGzK8+KLL6aISO+//36FY+6+++7UqFGjtTu5dai843LSSSelfv36rdF2NtVzpl+/fmm//fardMzGds6ktPLfaM81lVtrr0h+8cUX8fLLL8eBBx5YZvmBBx4Yzz//fLnrjB8/fqXxBx10ULz00kuxdOnStTW19c68efMiImKLLbZY5dhddtklWrRoEfvvv3+MGTOmqqe2TkydOjVatmwZ7du3j2OOOSbee++9CsduiufMF198Effff3+ccsopUVRUVOnYTeF8KTVt2rSYPXt2mfOhTp060atXrwqfcyIqPocqW2djMG/evCgqKorGjRtXOu6zzz6Ltm3bRqtWreKwww6LSZMmVc8Eq9HYsWNjyy23jO222y5OO+20+OijjyodvymeM3PmzImRI0fGD3/4w1WO3djOmRX/RnuuqdxaC8mPP/44li1bFltttVWZ5VtttVXMnj273HVmz55d7vgvv/wyPv7447U1tfVKSikuvPDC2HvvvaNLly4VjmvRokX84Q9/iIcffjiGDx8eHTt2jP333z+eeeaZapxt1dtzzz3j3nvvjaeeeipuv/32mD17duy1114xd+7ccsdviufMiBEj4tNPP40f/OAHFY7ZVM6Xryt9XlmT55zS9dZ0nQ3d4sWL45JLLoljjz02GjZsWOG4Tp06xdChQ+PRRx+NYcOGRd26daNnz54xderUapxt1TrkkEPij3/8Y/ztb3+LX/7ylzFx4sTYb7/9YsmSJRWusymeM/fcc080aNAgjjjiiErHbWznTHl/oz3XVK7m2t7giq+YpJQqfRWlvPHlLd9YnHPOOfH3v/89nn322UrHdezYMTp27Fi43aNHj5g5c2bceOONse+++1b1NKvNIYccUvj3rl27Ro8ePWLbbbeNe+65Jy688MJy19nUzpk777wzDjnkkGjZsmWFYzaV86U8a/qck7vOhmrp0qVxzDHHxPLly2PIkCGVju3evXuZC0969uwZu+66a9x8883x29/+tqqnWi2OPvrowr936dIlunXrFm3bto2RI0dWGk2b0jkTEXHXXXfFcccdt8rPOm5s50xlf6M915Rvrb0i2bRp06hRo8ZKpf3RRx+tVOSlmjdvXu74mjVrRpMmTdbW1NYb5557bjz66KMxZsyYaNWq1Rqv37179w32v/JWV0lJSXTt2rXCx7mpnTPvv/9+/PWvf41TTz11jdfd2M+X0qv71+Q5p3S9NV1nQ7V06dIYMGBATJs2LUaPHl3pq5HlKS4ujt13332jPo9atGgRbdu2rfQxbkrnTETEuHHjYsqUKVnPOxvyOVPR32jPNZVbayFZu3bt2G233QpXl5YaPXp07LXXXuWu06NHj5XGjxo1Krp16xa1atVaW1Nb51JKcc4558Tw4cPjb3/7W7Rv3z5rO5MmTYoWLVqs5dmtX5YsWRKTJ0+u8HFuKudMqbvvvju23HLL6Nu37xqvu7GfL+3bt4/mzZuXOR+++OKLePrppyt8zomo+ByqbJ0NUWlETp06Nf76179m/YdWSileffXVjfo8mjt3bsycObPSx7ipnDOl7rzzzthtt91ip512WuN1N8RzZlV/oz3XrMLavHLnf/7nf1KtWrXSnXfemd566610wQUXpJKSkjR9+vSUUkqXXHJJOuGEEwrj33vvvVS/fv304x//OL311lvpzjvvTLVq1UoPPfTQ2pzWOnfmmWemRo0apbFjx6ZZs2YVfhYtWlQYs+Kx+dWvfpUeeeSR9I9//CO98cYb6ZJLLkkRkR5++OF18RCqzEUXXZTGjh2b3nvvvTRhwoR02GGHpQYNGmzy50xKKS1btiy1adMmDRw4cKX7NpXzZcGCBWnSpElp0qRJKSLSTTfdlCZNmlS48njw4MGpUaNGafjw4en1119P3//+91OLFi3S/PnzC9s44YQTynxzxHPPPZdq1KiRBg8enCZPnpwGDx6catasmSZMmFDtj++bqOzYLF26NH3nO99JrVq1Sq+++mqZ550lS5YUtrHisRk0aFB68skn07vvvpsmTZqUTj755FSzZs30wgsvrIuHmKWy47JgwYJ00UUXpeeffz5NmzYtjRkzJvXo0SNtvfXWm/w5U2revHmpfv366Xe/+12529gYz5nV+Ru9KT/XrMpaDcmUUrr11ltT27ZtU+3atdOuu+5a5ituTjrppNSrV68y48eOHZt22WWXVLt27dSuXbsKT94NWUSU+3P33XcXxqx4bK677rq07bbbprp166bNN9887b333mnkyJHVP/kqdvTRR6cWLVqkWrVqpZYtW6Yjjjgivfnmm4X7N9VzJqWUnnrqqRQRacqUKSvdt6mcL6Vfa7Tiz0knnZRS+uprOa688srUvHnzVKdOnbTvvvum119/vcw2evXqVRhf6sEHH0wdO3ZMtWrVSp06ddogg7uyYzNt2rQKn3fGjBlT2MaKx+aCCy5Ibdq0SbVr107NmjVLBx54YHr++eer/8F9A5Udl0WLFqUDDzwwNWvWLNWqVSu1adMmnXTSSWnGjBlltrEpnjOlfv/736d69eqlTz/9tNxtbIznzOr8jd6Un2tWpSil/7tSAQAA1oD/1zYAAFmEJAAAWYQkAABZhCQAAFmEJAAAWYQkAABZhCQAAFmEJAAAWYQksMHq3bt3XHDBBRvctgE2FkIS2KSNHTs2ioqK4tNPP13XUwHY4AhJgLVk6dKl63oKANVKSAIbtC+//DLOOeecaNy4cTRp0iQuv/zySCkV7r///vujW7du0aBBg2jevHkce+yx8dFHH0VExPTp06NPnz4REbH55ptHUVFR/OAHPyisu3z58rj44otjiy22iObNm8egQYPK7LuoqChuu+226NevX5SUlMTVV18dERG/+93vYtttt43atWtHx44d47777iuz3owZM6Jfv36x2WabRcOGDWPAgAExZ86cwv2DBg2KnXfeOe66665o06ZNbLbZZnHmmWfGsmXL4vrrr4/mzZvHlltuGb/4xS/W5qEEWGNCEtig3XPPPVGzZs144YUX4re//W386le/ijvuuKNw/xdffBE///nP47XXXosRI0bEtGnTCrHYunXrePjhhyMiYsqUKTFr1qz4zW9+U2bbJSUl8cILL8T1118f//Vf/xWjR48us/8rr7wy+vXrF6+//nqccsop8cgjj8T5558fF110UbzxxhtxxhlnxMknnxxjxoyJiIiUUvTv3z/+/e9/x9NPPx2jR4+Od999N44++ugy23333XfjiSeeiCeffDKGDRsWd911V/Tt2zc++OCDePrpp+O6666Lyy+/PCZMmFAVhxVg9SSADVSvXr1S586d0/LlywvLBg4cmDp37lzhOi+++GKKiLRgwYKUUkpjxoxJEZE++eSTlba99957l1m2++67p4EDBxZuR0S64IILyozZa6+90mmnnVZm2VFHHZUOPfTQlFJKo0aNSjVq1EgzZswo3P/mm2+miEgvvvhiSimlK6+8MtWvXz/Nnz+/MOaggw5K7dq1S8uWLSss69ixY7r22msrfKwAVc0rksAGrXv37lFUVFS43aNHj5g6dWosW7YsIiImTZoU/fr1i7Zt20aDBg2id+/eEfHV28ursuOOO5a53aJFi8Lb4qW6detW5vbkyZOjZ8+eZZb17NkzJk+eXLi/devW0bp168L922+/fTRu3LgwJiKiXbt20aBBg8LtrbbaKrbffvsoLi4us2zF+QBUJyEJbLQWLlwYBx54YGy22WZx//33x8SJE+ORRx6JiK/e8l6VWrVqlbldVFQUy5cvL7OspKRkpfW+HrYRX72dXbrs6/9e0ZiK9r068wGoTkIS2KCt+BnBCRMmxLe+9a2oUaNGvP322/Hxxx/H4MGDY5999olOnTqt9Ape7dq1IyIKr2B+U507d45nn322zLLnn38+OnfuHBFfvfo4Y8aMmDlzZuH+t956K+bNm1cYA7ChEJLABm3mzJlx4YUXxpQpU2LYsGFx8803x/nnnx8REW3atInatWvHzTffHO+99148+uij8fOf/7zM+m3bto2ioqJ47LHH4l//+ld89tln32g+P/3pT2Po0KFx2223xdSpU+Omm26K4cOHx09+8pOIiDjggANixx13jOOOOy5eeeWVePHFF+PEE0+MXr16rfQ2OcD6TkgCG7QTTzwxPv/889hjjz3i7LPPjnPPPTdOP/30iIho1qxZDB06NB588MHYfvvtY/DgwXHjjTeWWX/rrbeOq666Ki655JLYaqut4pxzzvlG8+nfv3/85je/iRtuuCF22GGH+P3vfx9333134bOZRUVFMWLEiNh8881j3333jQMOOCC22WabeOCBB77RfgHWhaKUvvaFawAAsJq8IgkAQBYhCQBAFiEJAEAWIQkAQBYhCQBAFiEJAEAWIQkAQBYhCQBAFiEJAEAWIQkAQBYhCQBAlv8PkT2mLUamjf4AAAAASUVORK5CYII=",
      "text/plain": [
       "<Figure size 800x600 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Create a box plot\n",
    "plt.figure(figsize=(8, 6))\n",
    "plt.boxplot(df['bathroom'], vert=False)\n",
    "plt.title('Box Plot of Property Size')\n",
    "plt.xlabel('bathroom ')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>rent</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>bathroom</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1.0</th>\n",
       "      <td>12180.735551</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2.0</th>\n",
       "      <td>20053.154924</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3.0</th>\n",
       "      <td>29102.111511</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4.0</th>\n",
       "      <td>34170.370370</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5.0</th>\n",
       "      <td>34000.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>21.0</th>\n",
       "      <td>27000.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                  rent\n",
       "bathroom              \n",
       "1.0       12180.735551\n",
       "2.0       20053.154924\n",
       "3.0       29102.111511\n",
       "4.0       34170.370370\n",
       "5.0       34000.000000\n",
       "21.0      27000.000000"
      ]
     },
     "execution_count": 80,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[['bathroom','rent']].groupby(['bathroom']).mean()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Facing"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "E     8264\n",
       "N     5042\n",
       "W     2300\n",
       "S     1013\n",
       "NE     709\n",
       "SE     163\n",
       "NW     126\n",
       "SW      50\n",
       "Name: facing, dtype: int64"
      ]
     },
     "execution_count": 81,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['facing'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>rent</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>facing</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>E</th>\n",
       "      <td>18937.869555</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>N</th>\n",
       "      <td>17731.770131</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>NE</th>\n",
       "      <td>21456.623413</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>NW</th>\n",
       "      <td>21654.761905</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>S</th>\n",
       "      <td>18443.139191</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>SE</th>\n",
       "      <td>21407.668712</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>SW</th>\n",
       "      <td>23550.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>W</th>\n",
       "      <td>20359.890870</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                rent\n",
       "facing              \n",
       "E       18937.869555\n",
       "N       17731.770131\n",
       "NE      21456.623413\n",
       "NW      21654.761905\n",
       "S       18443.139191\n",
       "SE      21407.668712\n",
       "SW      23550.000000\n",
       "W       20359.890870"
      ]
     },
     "execution_count": 82,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[['facing','rent']].groupby(['facing']).mean()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<seaborn.axisgrid.JointGrid at 0x25b714b4460>"
      ]
     },
     "execution_count": 83,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 600x600 with 3 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.jointplot(x = 'facing', y = 'rent', data = df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "metadata": {},
   "outputs": [],
   "source": [
    "label_encoder = LabelEncoder()\n",
    "df['facing_encoded'] = label_encoder.fit_transform(df['facing'])\n",
    "df.drop(columns=['facing'], inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1.0     5102\n",
       "0.0     4136\n",
       "2.0     3914\n",
       "3.0     2284\n",
       "4.0     1061\n",
       "5.0      263\n",
       "6.0      179\n",
       "7.0      158\n",
       "9.0      116\n",
       "8.0      108\n",
       "10.0      92\n",
       "11.0      78\n",
       "12.0      53\n",
       "14.0      39\n",
       "13.0      29\n",
       "15.0      17\n",
       "16.0      16\n",
       "17.0       8\n",
       "19.0       5\n",
       "18.0       4\n",
       "20.0       3\n",
       "25.0       1\n",
       "22.0       1\n",
       "Name: floor, dtype: int64"
      ]
     },
     "execution_count": 85,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['floor'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='floor', ylabel='Count'>"
      ]
     },
     "execution_count": 86,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.histplot(data=df, x=\"floor\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "4.0     4307\n",
       "3.0     4024\n",
       "2.0     4014\n",
       "1.0     1714\n",
       "5.0     1365\n",
       "0.0      281\n",
       "14.0     224\n",
       "9.0      189\n",
       "12.0     185\n",
       "6.0      185\n",
       "8.0      168\n",
       "10.0     167\n",
       "11.0     166\n",
       "13.0     163\n",
       "7.0      149\n",
       "15.0     111\n",
       "16.0      63\n",
       "19.0      59\n",
       "18.0      48\n",
       "17.0      32\n",
       "20.0      20\n",
       "21.0      11\n",
       "23.0       8\n",
       "24.0       6\n",
       "25.0       4\n",
       "22.0       2\n",
       "26.0       2\n",
       "Name: total_floor, dtype: int64"
      ]
     },
     "execution_count": 87,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['total_floor'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAq8AAAIhCAYAAABg21M1AAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/YYfK9AAAACXBIWXMAAA9hAAAPYQGoP6dpAABdMUlEQVR4nO3df3yU5Z3v/3ckk8wkmRlDokAEIpqgVgL1V62YxmqPtGxrNea01rYW3LO2noo9St1FsFasCqhHura2tfZsQU+1pV1E7epp64qAILpUUVKlmtQfQANixjATkgxJ4Pr+4XdG4ySTZDLXzFzh9Xw88njIfU0+8+b+NR+H+77uPGOMEQAAAOCAI7IdAAAAABgqmlcAAAA4g+YVAAAAzqB5BQAAgDNoXgEAAOAMmlcAAAA4g+YVAAAAzqB5BQAAgDNoXgEAAOAMmlfAUc8//7zq6+s1efJkFRYWaty4cTrrrLP03e9+19p7Pvvss1q8eLH27duXMPbTn/5UK1eutPbe/fn0pz+tvLy8+I/P59OMGTP0r//6rzp06FD8dXPnztWxxx6b0nuk4+/V0tKixYsX66WXXkq5RrJ1P1SLFy9WXl7esH9v1apVOvnkk+Xz+ZSXl6eXXnop5Vqu+/GPf6yqqioVFBQoLy9P+/btG9H+BWD4aF4BBz3++OOaOXOmIpGI7rjjDv3pT3/S3XffrbPPPlurVq2y9r7PPvusbr755pxpXiXpuOOO0+bNm7V582atWrVKxxxzjK699lotXLgwLfXT1bzefPPNI25eB1r3Nr377ru67LLLdPzxx+sPf/iDNm/erKlTp2Y0Q6546aWX9J3vfEfnnnuu1q5dq82bN8vv92c7FnDYyc92AADDd8cdd2jKlCn64x//qPz8Dw7jr3zlK7rjjjuymCy9jDGKRqPy+XwDvsbn8+mTn/xk/M+zZ8/WiSeeqHvuuUe33nqrPB5PJqKOWq+//rp6enr09a9/Xeecc06246izs1NFRUVZee9XXnlFknTFFVfoE5/4RFYyfFg21wWQTXzzCjgoFAqpvLy8T+Mac8QRiYf1Qw89pLPOOkslJSUqKSnRxz/+cf3bv/1bfPzJJ5/UhRdeqIkTJ8rr9aqqqkrf+ta31NraGn/N4sWL9c///M+SpClTpsT/qX7dunU69thj9corr2j9+vXx5R/+Z9RIJKLrrrtOU6ZMUUFBgY455hhdc8016ujo6JMzLy9P8+bN07333quTTjpJhYWFuv/++4e1bjwej0477TR1dnbq3XffHfB10WhUCxcu7JPpqquu6vPN5mB/r6FYt26dzjjjDEnS5ZdfHq+zePHi+Gsee+wxnXXWWSoqKpLf79f555+vzZs3x8eTrXvp/X/WnzVrliZMmCCfz6eTTjpJ119/fcL6Ha65c+eqtrZWknTJJZcoLy9Pn/70pwd8/aFDh3THHXfoxBNPVGFhoY4++mh94xvf0K5duxJe+8tf/lIzZsyQ1+vV2LFjVV9fr+3btye8f0lJiRobGzVr1iz5/X595jOf6fe9H3nkEeXl5empp55KGPvZz36mvLw8bdu2TZL0xhtv6Ctf+YoqKiril9x85jOfSfrN+Kc//Wl9/etflySdeeaZysvL09y5cwd8/VD2r+Gss09/+tOaNm2aNmzYoJkzZ6qoqEj/+I//OOD7A6OaAeCcf/qnfzKSzNVXX22ee+45093dPeBrb7zxRiPJXHzxxeZ3v/ud+dOf/mSWL19ubrzxxvhrfvazn5mlS5eaxx57zKxfv97cf//9ZsaMGeaEE06I1965c6e5+uqrjSTz8MMPm82bN5vNmzebcDhsXnzxRXPccceZU045Jb78xRdfNMYY09HRYT7+8Y+b8vJys3z5cvOf//mf5u677zbBYNCcd9555tChQ/Eckswxxxxjpk+fbh566CGzdu1a85e//GXAv9s555xjTj755ITlp556qsnPzzednZ3GGGPmzJljKisr4+OHDh0yn/3sZ01+fr658cYbzZ/+9Cfzv//3/zbFxcXmlFNOMdFo1Bhjkv69Yu8/2Gk0HA6bFStWGEnme9/7XrzOzp07jTHGPPjgg0aSmTVrlnnkkUfMqlWrzGmnnWYKCgrMM888M+i6N8aYW265xfzwhz80jz/+uFm3bp259957zZQpU8y5557bJ8tNN900aN4Pa25uNj/5yU+MJLNkyRKzefNm88orrwxY65vf/KaRZObNm2f+8Ic/mHvvvdccddRRZtKkSebdd9+Nv27JkiVGkrn00kvN448/bh544AFz3HHHmWAwaF5//fX46+bMmWM8Ho859thjzdKlS81TTz1l/vjHP/abtaenxxx99NHma1/7WsLYJz7xCXPqqafG/3zCCSeYqqoq83//7/8169evN6tXrzbf/e53zdNPPz3gunjllVfM9773PSPJrFixwmzevNk0NzfHc6ayfw1nnZ1zzjlm7NixZtKkSebHP/6xefrpp8369esHzAuMZjSvgINaW1tNbW2tkWQkGY/HY2bOnGmWLl1q2tvb46974403zJgxY/r9QB/IoUOHTE9Pj3n77beNJPPoo4/Gx+68804jybz55psJv3fyySebc845J2H50qVLzRFHHGG2bNnSZ/m///u/G0nmiSeeiC+TZILBoHnvvfeGlDXWvPb09Jienh7T0tJirr/+eiPJfOlLX4q/7qPNxR/+8Acjydxxxx196q1atcpIMvfdd9+gfy9jjDnvvPPMmDFjBs25ZcuWeNPzYQcPHjQVFRWmpqbGHDx4ML68vb3dHH300WbmzJnxZcnW/YfFtt/69euNJPPyyy/Hx4bbvBpjzNNPP20kmd/97nd9ln+01vbt240k8+1vf7vP655//nkjySxatMgYY0xbW5vx+XzmH/7hH/q8bseOHaawsNB89atfjS+bM2eOkWR++ctfDinr/Pnzjc/nM/v27Ysve/XVV40k8+Mf/9gY8/6xI8n867/+65Bqfljsf0I+ui+nun8NdZ0Z88H/KD311FPDzg2MNlw2ADiorKxMzzzzjLZs2aJly5bpwgsv1Ouvv66FCxeqpqYm/s/9Tz75pA4ePKirrroqab29e/fqyiuv1KRJk5Sfny+Px6PKykpJSvin3OH6j//4D02bNk0f//jH1dvbG//57Gc/2+efvmPOO+88lZaWDrn+K6+8Io/HI4/Ho4qKCt1111362te+pl/84hcD/s7atWslKeGffb/0pS+puLi433967s9TTz2l3t7eIWf9qNdee00tLS267LLL+lzuUVJSooaGBj333HPq7OwctM4bb7yhr371qxo/frzGjBkjj8cTvz51pNtvqJ5++mlJiev0E5/4hE466aT4Ot28ebO6uroSXjdp0iSdd955/a77hoaGIWX4x3/8R3V1dfW5aXHFihUqLCzUV7/6VUnS2LFjdfzxx+vOO+/U8uXLtXXr1j4zU6TDUPevoa6zmNLSUp133nlpzQq4iOYVcNjpp5+uBQsW6He/+51aWlp07bXX6q233orftBW75nPixIkD1jh06JBmzZqlhx9+WP/yL/+ip556Sv/1X/+l5557TpLU1dU1oozvvPOOtm3bFm8wYz9+v1/GmD7X1UrShAkThlX/+OOP15YtW/TnP/9Zf/nLX7Rv3z796le/UjAYHPB3QqGQ8vPzddRRR/VZnpeXp/HjxysUCg0rQ6pi79Pf37miokKHDh1SW1tb0hr79+/Xpz71KT3//PO69dZbtW7dOm3ZskUPP/ywpJFvv6Ea7O8SGx/q62KKiooUCASGlOHkk0/WGWecoRUrVkiSDh48qF/96le68MILNXbsWEmKXxf72c9+VnfccYdOPfVUHXXUUfrOd76j9vb2If5tkxvq/jXcdTHcYwMYrZhtABglPB6PbrrpJv3whz/UX/7yF0mKf3ju2rVLkyZN6vf3/vKXv+jll1/WypUrNWfOnPjy5ubmtOQqLy+Xz+fTL3/5ywHHP2y4c4d6vV6dfvrpw/qdsrIy9fb26t133+3TYBhjtGfPnvgNVraVlZVJknbv3p0w1tLSoiOOOGLQb6HXrl2rlpYWrVu3rs9sAJmeUuvDf5eP/s9SS0tLfDsP9nce6f5w+eWX69vf/ra2b9+uN954Q7t379bll1/e5zWVlZXxGxZff/11/fa3v9XixYvV3d2te++9d1jv15+h7l9DXWcxh+O8ukB/+OYVcFB/H/zSB/9EXFFRIUmaNWuWxowZo5/97GcD1op9IBYWFvZZ/vOf/zzhtbHX9PdtXmFhYb/Lv/CFL+hvf/ubysrKdPrppyf8ZGNy99gd67/61a/6LF+9erU6Ojr63NE+0N9rOAZabyeccIKOOeYYPfTQQzLGxJd3dHRo9erV8RkIktUYzvazKfbP2R9dp1u2bNH27dvj6/Sss86Sz+dLeN2uXbu0du3aAWcTGKpLL71UXq9XK1eu1MqVK3XMMcdo1qxZA75+6tSp+t73vqeamhq9+OKLI3rvmKHuX0NdZwD64ptXwEGf/exnNXHiRF1wwQU68cQTdejQIb300ku66667VFJSov/1v/6XpPenelq0aJFuueUWdXV16dJLL1UwGNSrr76q1tZW3XzzzTrxxBN1/PHH6/rrr5cxRmPHjtXvf/97PfnkkwnvW1NTI0m6++67NWfOHHk8Hp1wwgny+/2qqanRb37zG61atUrHHXecvF6vampqdM0112j16tWqq6vTtddeq+nTp+vQoUPasWOH/vSnP+m73/2uzjzzzIyuv/PPP1+f/exntWDBAkUiEZ199tnatm2bbrrpJp1yyim67LLL+vyd+/t7Se83KevXrx/0utfjjz9ePp9PDz74oE466SSVlJSooqJCFRUVuuOOO/S1r31NX/jCF/Stb31LBw4c0J133ql9+/Zp2bJlfXJIiet+5syZKi0t1ZVXXqmbbrpJHo9HDz74oF5++WULa25gJ5xwgr75zW/qxz/+sY444gjNnj1bb731lm688UZNmjRJ1157rSTpyCOP1I033qhFixbpG9/4hi699FKFQiHdfPPN8nq9uummm0aU48gjj1R9fb1Wrlypffv26brrrutzPfG2bds0b948felLX1J1dbUKCgq0du1abdu2Tddff/2I3jtmqPvXUNcZgI/I6u1iAFKyatUq89WvftVUV1ebkpIS4/F4zOTJk81ll11mXn311YTXP/DAA+aMM84wXq/XlJSUmFNOOaXPne+vvvqqOf/8843f7zelpaXmS1/6ktmxY4eRZG666aY+tRYuXGgqKirMEUccYSTFpxd66623zKxZs4zf7zeS+tx9vX//fvO9733PnHDCCaagoMAEg0FTU1Njrr32WrNnz5746ySZq666asjrYaCpsj7qo3eDG2NMV1eXWbBggamsrDQej8dMmDDB/M//+T9NW1tbn9cl+3sNZaqsmF//+tfmxBNPNB6PJ2G9PvLII+bMM880Xq/XFBcXm8985jNm06ZNCTUGWvfPPvusOeuss0xRUZE56qijzD/90z+ZF198MWGGA5uzDRjz/uwJt99+u5k6darxeDymvLzcfP3rX49PC/Zh/+f//B8zffr0+P5w4YUXxqfhipkzZ44pLi4eVl5jjPnTn/4Un4njw1NvGWPMO++8Y+bOnWtOPPFEU1xcbEpKSsz06dPND3/4Q9Pb25u07lBnGzBm6PvXUNfZUPd14HCQZ8yH/q0KAAAAyGFc8woAAABncM0rAByGDh06NOj8pv09fhgAso1vXgHgMPSDH/wgYe7dj/689dZb2Y4JAAm45hUADkMtLS1qaWlJ+prp06eroKAgQ4kAYGhoXgEAAOAMLhsAAACAM0b91fiHDh1SS0uL/H4/j9YDAADIQcYYtbe3q6Kios+DRfoz6pvXlpaWAZ/pDgAAgNyxc+dOTZw4MelrRn3z6vf7Jb2/MgKBQJbTAAAA4KMikYgmTZoU79uSGfXNa+xSgUAgQPMKAACQw4ZyiSc3bAEAAMAZNK8A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PVa33nqr5s6dq2AwqCuuuMLmXwsArKJ5BYAsufvuu/WDH/xAEydO1O7du7Vly5aE18ydO1d//vOf9dhjj2nz5s0yxugf/uEf1NPTI0l64YUX9OUvf1lf+cpX1NjYqMWLF+vGG2/UypUr+9S58847NW3aNL3wwgu68cYbM/HXAwAruGwAALIkGAzK7/drzJgxGj9+fMJ4U1OTHnvsMW3atCl+WcGDDz6oSZMm6ZFHHtGXvvQlLV++XJ/5zGfiDenUqVP16quv6s4779TcuXPjtc477zxdd911Gfl7AYBNfPMKADlq+/btys/P15lnnhlfVlZWphNOOEHbt2+Pv+bss8/u83tnn322mpqadPDgwfiy008/PTOhAcAymlcAyFHGmAGX5+XlJfx3st8rLi5Of0AAyAKaVwDIUR/72MfU29ur559/Pr4sFArp9ddf10knnRR/zcaNG/v83rPPPqupU6dqzJgxGc0LAJlA8woAOaq6uloXXnihrrjiCm3cuFEvv/yyvv71r+uYY47RhRdeKEn67ne/q6eeekq33HKLXn/9dd1///265557uL4VwKhF8woAOWzFihU67bTT9IUvfEFnnXWWjDF64okn5PF4JEmnnnqqfvvb3+o3v/mNpk2bpu9///v6wQ9+0OdmLQAYTfLMQBdVAQAAADmGb14BAADgDJpXAAAAOIPmFQAAAM6geQUAAIAzaF4BAADgDJpXAAAAOIPmFQAAAM6geQUAAIAzaF4BAADgDJpXAAAAOIPmFQAAAM74/wCex6cRk2rYugAAAABJRU5ErkJggg==",
      "text/plain": [
       "<Figure size 800x600 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(8, 6))\n",
    "sns.scatterplot(x=df['floor'], y=df['total_floor'])\n",
    "plt.title(\"Scatter Plot: {} vs {}\".format('total_floor', 'floor'))\n",
    "plt.xlabel('floor')\n",
    "plt.ylabel('total_floor')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1.0     6927\n",
       "0.0     4933\n",
       "2.0     4153\n",
       "3.0     1383\n",
       "4.0      243\n",
       "5.0       25\n",
       "13.0       1\n",
       "6.0        1\n",
       "10.0       1\n",
       "Name: balconies, dtype: int64"
      ]
     },
     "execution_count": 89,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['balconies'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "metadata": {},
   "outputs": [],
   "source": [
    "df.drop(columns = ['id'], inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(17667, 34)"
      ]
     },
     "execution_count": 91,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "Int64Index: 17667 entries, 0 to 20554\n",
      "Data columns (total 34 columns):\n",
      " #   Column                 Non-Null Count  Dtype  \n",
      "---  ------                 --------------  -----  \n",
      " 0   latitude               17667 non-null  float64\n",
      " 1   longitude              17667 non-null  float64\n",
      " 2   property_size          17667 non-null  float64\n",
      " 3   bathroom               17667 non-null  float64\n",
      " 4   floor                  17667 non-null  float64\n",
      " 5   total_floor            17667 non-null  float64\n",
      " 6   balconies              17667 non-null  float64\n",
      " 7   rent                   17667 non-null  float64\n",
      " 8   LIFT                   17667 non-null  int64  \n",
      " 9   GYM                    17667 non-null  int64  \n",
      " 10  AC                     17667 non-null  int64  \n",
      " 11  CLUB                   17667 non-null  int64  \n",
      " 12  INTERCOM               17667 non-null  int64  \n",
      " 13  POOL                   17667 non-null  int64  \n",
      " 14  CPA                    17667 non-null  int64  \n",
      " 15  FS                     17667 non-null  int64  \n",
      " 16  SERVANT                17667 non-null  int64  \n",
      " 17  SECURITY               17667 non-null  int64  \n",
      " 18  GP                     17667 non-null  int64  \n",
      " 19  PARK                   17667 non-null  int64  \n",
      " 20  RWH                    17667 non-null  int64  \n",
      " 21  STP                    17667 non-null  int64  \n",
      " 22  HK                     17667 non-null  int64  \n",
      " 23  PB                     17667 non-null  int64  \n",
      " 24  VP                     17667 non-null  int64  \n",
      " 25  age_of_property        17667 non-null  int64  \n",
      " 26  lease_type_encoded     17667 non-null  int32  \n",
      " 27  furnishing_encoded     17667 non-null  int32  \n",
      " 28  parking_encoded        17667 non-null  int32  \n",
      " 29  water_supply_encoded   17667 non-null  int32  \n",
      " 30  building_type_encoded  17667 non-null  int32  \n",
      " 31  BHK_type_encoded       17667 non-null  int32  \n",
      " 32  locality_encoded       17667 non-null  int32  \n",
      " 33  facing_encoded         17667 non-null  int32  \n",
      "dtypes: float64(8), int32(8), int64(18)\n",
      "memory usage: 4.2 MB\n"
     ]
    }
   ],
   "source": [
    "df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>latitude</th>\n",
       "      <th>longitude</th>\n",
       "      <th>property_size</th>\n",
       "      <th>bathroom</th>\n",
       "      <th>floor</th>\n",
       "      <th>total_floor</th>\n",
       "      <th>balconies</th>\n",
       "      <th>rent</th>\n",
       "      <th>LIFT</th>\n",
       "      <th>GYM</th>\n",
       "      <th>...</th>\n",
       "      <th>PB</th>\n",
       "      <th>VP</th>\n",
       "      <th>age_of_property</th>\n",
       "      <th>lease_type_encoded</th>\n",
       "      <th>furnishing_encoded</th>\n",
       "      <th>parking_encoded</th>\n",
       "      <th>water_supply_encoded</th>\n",
       "      <th>building_type_encoded</th>\n",
       "      <th>BHK_type_encoded</th>\n",
       "      <th>locality_encoded</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>17667.000000</td>\n",
       "      <td>17667.000000</td>\n",
       "      <td>17667.000000</td>\n",
       "      <td>17667.000000</td>\n",
       "      <td>17667.000000</td>\n",
       "      <td>17667.000000</td>\n",
       "      <td>17667.000000</td>\n",
       "      <td>17667.000000</td>\n",
       "      <td>17667.000000</td>\n",
       "      <td>17667.000000</td>\n",
       "      <td>...</td>\n",
       "      <td>17667.000000</td>\n",
       "      <td>17667.000000</td>\n",
       "      <td>17667.000000</td>\n",
       "      <td>17667.000000</td>\n",
       "      <td>17667.000000</td>\n",
       "      <td>17667.000000</td>\n",
       "      <td>17667.000000</td>\n",
       "      <td>17667.000000</td>\n",
       "      <td>17667.000000</td>\n",
       "      <td>17667.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>12.945511</td>\n",
       "      <td>77.637230</td>\n",
       "      <td>1035.396219</td>\n",
       "      <td>1.838512</td>\n",
       "      <td>1.906775</td>\n",
       "      <td>3.871229</td>\n",
       "      <td>1.160808</td>\n",
       "      <td>18906.717836</td>\n",
       "      <td>0.409577</td>\n",
       "      <td>0.256127</td>\n",
       "      <td>...</td>\n",
       "      <td>0.377200</td>\n",
       "      <td>0.244184</td>\n",
       "      <td>5.048622</td>\n",
       "      <td>1.521028</td>\n",
       "      <td>1.816890</td>\n",
       "      <td>1.209883</td>\n",
       "      <td>1.367578</td>\n",
       "      <td>1.208638</td>\n",
       "      <td>1.153110</td>\n",
       "      <td>65.924209</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>0.029318</td>\n",
       "      <td>0.071526</td>\n",
       "      <td>404.911914</td>\n",
       "      <td>0.676726</td>\n",
       "      <td>2.201029</td>\n",
       "      <td>3.189530</td>\n",
       "      <td>0.980916</td>\n",
       "      <td>8031.712341</td>\n",
       "      <td>0.491770</td>\n",
       "      <td>0.436505</td>\n",
       "      <td>...</td>\n",
       "      <td>0.484699</td>\n",
       "      <td>0.429615</td>\n",
       "      <td>0.471852</td>\n",
       "      <td>1.478801</td>\n",
       "      <td>0.516162</td>\n",
       "      <td>1.388518</td>\n",
       "      <td>0.737128</td>\n",
       "      <td>1.132483</td>\n",
       "      <td>0.910424</td>\n",
       "      <td>40.881470</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>12.900004</td>\n",
       "      <td>77.500177</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>8000.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>...</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>4.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>12.918288</td>\n",
       "      <td>77.574020</td>\n",
       "      <td>700.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>12500.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>...</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>5.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>26.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>12.943465</td>\n",
       "      <td>77.637235</td>\n",
       "      <td>1050.000000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>17500.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>...</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>5.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>66.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>12.970715</td>\n",
       "      <td>77.698906</td>\n",
       "      <td>1263.000000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>4.000000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>24000.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>...</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>5.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>99.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>12.999999</td>\n",
       "      <td>77.852451</td>\n",
       "      <td>2200.000000</td>\n",
       "      <td>21.000000</td>\n",
       "      <td>25.000000</td>\n",
       "      <td>26.000000</td>\n",
       "      <td>13.000000</td>\n",
       "      <td>50000.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>...</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>6.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>5.000000</td>\n",
       "      <td>134.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>8 rows × 33 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "           latitude     longitude  property_size      bathroom         floor  \\\n",
       "count  17667.000000  17667.000000   17667.000000  17667.000000  17667.000000   \n",
       "mean      12.945511     77.637230    1035.396219      1.838512      1.906775   \n",
       "std        0.029318      0.071526     404.911914      0.676726      2.201029   \n",
       "min       12.900004     77.500177       1.000000      1.000000      0.000000   \n",
       "25%       12.918288     77.574020     700.000000      1.000000      1.000000   \n",
       "50%       12.943465     77.637235    1050.000000      2.000000      1.000000   \n",
       "75%       12.970715     77.698906    1263.000000      2.000000      3.000000   \n",
       "max       12.999999     77.852451    2200.000000     21.000000     25.000000   \n",
       "\n",
       "        total_floor     balconies          rent          LIFT           GYM  \\\n",
       "count  17667.000000  17667.000000  17667.000000  17667.000000  17667.000000   \n",
       "mean       3.871229      1.160808  18906.717836      0.409577      0.256127   \n",
       "std        3.189530      0.980916   8031.712341      0.491770      0.436505   \n",
       "min        0.000000      0.000000   8000.000000      0.000000      0.000000   \n",
       "25%        2.000000      0.000000  12500.000000      0.000000      0.000000   \n",
       "50%        3.000000      1.000000  17500.000000      0.000000      0.000000   \n",
       "75%        4.000000      2.000000  24000.000000      1.000000      1.000000   \n",
       "max       26.000000     13.000000  50000.000000      1.000000      1.000000   \n",
       "\n",
       "       ...            PB            VP  age_of_property  lease_type_encoded  \\\n",
       "count  ...  17667.000000  17667.000000     17667.000000        17667.000000   \n",
       "mean   ...      0.377200      0.244184         5.048622            1.521028   \n",
       "std    ...      0.484699      0.429615         0.471852            1.478801   \n",
       "min    ...      0.000000      0.000000         4.000000            0.000000   \n",
       "25%    ...      0.000000      0.000000         5.000000            0.000000   \n",
       "50%    ...      0.000000      0.000000         5.000000            1.000000   \n",
       "75%    ...      1.000000      0.000000         5.000000            3.000000   \n",
       "max    ...      1.000000      1.000000         6.000000            3.000000   \n",
       "\n",
       "       furnishing_encoded  parking_encoded  water_supply_encoded  \\\n",
       "count        17667.000000     17667.000000          17667.000000   \n",
       "mean             1.816890         1.209883              1.367578   \n",
       "std              0.516162         1.388518              0.737128   \n",
       "min              0.000000         0.000000              0.000000   \n",
       "25%              2.000000         0.000000              1.000000   \n",
       "50%              2.000000         0.000000              2.000000   \n",
       "75%              2.000000         3.000000              2.000000   \n",
       "max              2.000000         3.000000              2.000000   \n",
       "\n",
       "       building_type_encoded  BHK_type_encoded  locality_encoded  \n",
       "count           17667.000000      17667.000000      17667.000000  \n",
       "mean                1.208638          1.153110         65.924209  \n",
       "std                 1.132483          0.910424         40.881470  \n",
       "min                 0.000000          0.000000          0.000000  \n",
       "25%                 0.000000          1.000000         26.000000  \n",
       "50%                 2.000000          1.000000         66.000000  \n",
       "75%                 2.000000          1.000000         99.000000  \n",
       "max                 3.000000          5.000000        134.000000  \n",
       "\n",
       "[8 rows x 33 columns]"
      ]
     },
     "execution_count": 93,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "latitude                 0\n",
       "longitude                0\n",
       "property_size            0\n",
       "bathroom                 0\n",
       "facing                   0\n",
       "floor                    0\n",
       "total_floor              0\n",
       "balconies                0\n",
       "rent                     0\n",
       "LIFT                     0\n",
       "GYM                      0\n",
       "AC                       0\n",
       "CLUB                     0\n",
       "INTERCOM                 0\n",
       "POOL                     0\n",
       "CPA                      0\n",
       "FS                       0\n",
       "SERVANT                  0\n",
       "SECURITY                 0\n",
       "GP                       0\n",
       "PARK                     0\n",
       "RWH                      0\n",
       "STP                      0\n",
       "HK                       0\n",
       "PB                       0\n",
       "VP                       0\n",
       "age_of_property          0\n",
       "lease_type_encoded       0\n",
       "furnishing_encoded       0\n",
       "parking_encoded          0\n",
       "water_supply_encoded     0\n",
       "building_type_encoded    0\n",
       "BHK_type_encoded         0\n",
       "locality_encoded         0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 97,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.isnull().sum()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Model Building"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 102,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Linear Regression (L2) - RMSE: 4580.715770892365\n",
      "Linear Regression (L1) - RMSE: 4580.693333029902\n",
      "Polynomial Regression - RMSE: 4797.908456974728\n",
      "Random Forest - RMSE: 3532.258016077102\n",
      "XGBoost - RMSE: 3416.8371565033276\n",
      "Support Vector Machines - RMSE: 4828.157457077213\n",
      "Ensemble Learning (Voting Regressor) - RMSE: 3899.4484688600865\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.preprocessing import StandardScaler, PolynomialFeatures\n",
    "from sklearn.linear_model import LinearRegression, Ridge, Lasso\n",
    "from sklearn.ensemble import RandomForestRegressor, VotingRegressor\n",
    "import xgboost as xgb\n",
    "from sklearn.svm import SVR\n",
    "from sklearn.metrics import mean_squared_error, r2_score\n",
    "#from tensorflow import keras\n",
    "#from keras.models import Sequential\n",
    "#from keras.layers import Dense\n",
    "#from keras.optimizers import Adam\n",
    "from sklearn.ensemble import BaggingRegressor, GradientBoostingRegressor\n",
    "\n",
    "# Load your dataset\n",
    "\n",
    "# Preprocessing\n",
    "# Handle missing values, encode categorical variables, etc.\n",
    "\n",
    "# Split the dataset into features (X) and target variable (y)\n",
    "X = df.drop(columns=['rent'])\n",
    "y = df['rent']\n",
    "\n",
    "# Split the data into training and testing sets\n",
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n",
    "\n",
    "# Feature Scaling\n",
    "scaler = StandardScaler()\n",
    "X_train_scaled = scaler.fit_transform(X_train)\n",
    "X_test_scaled = scaler.transform(X_test)\n",
    "\n",
    "# Linear Regression (L2)\n",
    "lin_reg = Ridge(alpha=1.0)\n",
    "lin_reg.fit(X_train_scaled, y_train)\n",
    "y_pred_lin_reg = lin_reg.predict(X_test_scaled)\n",
    "\n",
    "# Linear Regression (L1)\n",
    "lasso_reg = Lasso(alpha=0.1)\n",
    "lasso_reg.fit(X_train_scaled, y_train)\n",
    "y_pred_lasso_reg = lasso_reg.predict(X_test_scaled)\n",
    "\n",
    "# Polynomial Regression\n",
    "poly = PolynomialFeatures(degree=2)\n",
    "X_train_poly = poly.fit_transform(X_train_scaled)\n",
    "X_test_poly = poly.transform(X_test_scaled)\n",
    "poly_reg = LinearRegression()\n",
    "poly_reg.fit(X_train_poly, y_train)\n",
    "y_pred_poly_reg = poly_reg.predict(X_test_poly)\n",
    "\n",
    "# Random Forest\n",
    "rf_reg = RandomForestRegressor(n_estimators=100, random_state=42)\n",
    "rf_reg.fit(X_train_scaled, y_train)\n",
    "y_pred_rf_reg = rf_reg.predict(X_test_scaled)\n",
    "\n",
    "# XGBoost\n",
    "xgb_reg = xgb.XGBRegressor(n_estimators=100, learning_rate=0.1, random_state=42)\n",
    "xgb_reg.fit(X_train_scaled, y_train)\n",
    "y_pred_xgb_reg = xgb_reg.predict(X_test_scaled)\n",
    "\n",
    "# Artificial Neural Networks (ANN)\n",
    "# ann_model = Sequential()\n",
    "# ann_model.add(Dense(units=128, activation='relu', input_dim=X_train_scaled.shape[1]))\n",
    "# ann_model.add(Dense(units=64, activation='relu'))\n",
    "# ann_model.add(Dense(units=1))\n",
    "# ann_model.compile(optimizer=Adam(learning_rate=0.001), loss='mean_squared_error')\n",
    "# ann_model.fit(X_train_scaled, y_train, epochs=50, batch_size=32, verbose=0)\n",
    "# y_pred_ann = ann_model.predict(X_test_scaled)\n",
    "\n",
    "# Support Vector Machines (SVM)\n",
    "svm_reg = SVR(kernel='linear')\n",
    "svm_reg.fit(X_train_scaled, y_train)\n",
    "y_pred_svm_reg = svm_reg.predict(X_test_scaled)\n",
    "\n",
    "# Ensemble Learning (Voting Regressor)\n",
    "ensemble_model = VotingRegressor(estimators=[\n",
    "    ('lin_reg', lin_reg),\n",
    "    ('lasso_reg', lasso_reg),\n",
    "    ('rf_reg', rf_reg),\n",
    "    ('xgb_reg', xgb_reg),\n",
    "    ('svm_reg', svm_reg)\n",
    "])\n",
    "ensemble_model.fit(X_train_scaled, y_train)\n",
    "y_pred_ensemble = ensemble_model.predict(X_test_scaled)\n",
    "\n",
    "# Evaluate Models\n",
    "print(\"Linear Regression (L2) - RMSE:\", mean_squared_error(y_test, y_pred_lin_reg, squared=False))\n",
    "print(\"Linear Regression (L1) - RMSE:\", mean_squared_error(y_test, y_pred_lasso_reg, squared=False))\n",
    "print(\"Polynomial Regression - RMSE:\", mean_squared_error(y_test, y_pred_poly_reg, squared=False))\n",
    "print(\"Random Forest - RMSE:\", mean_squared_error(y_test, y_pred_rf_reg, squared=False))\n",
    "print(\"XGBoost - RMSE:\", mean_squared_error(y_test, y_pred_xgb_reg, squared=False))\n",
    "#print(\"Artificial Neural Networks - RMSE:\", mean_squared_error(y_test, y_pred_ann, squared=False))\n",
    "print(\"Support Vector Machines - RMSE:\", mean_squared_error(y_test, y_pred_svm_reg, squared=False))\n",
    "print(\"Ensemble Learning (Voting Regressor) - RMSE:\", mean_squared_error(y_test, y_pred_ensemble, squared=False))\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 103,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.8180867783402497"
      ]
     },
     "execution_count": 103,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "r2_score(y_test, y_pred_xgb_reg)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 112,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.8238001314893116"
      ]
     },
     "execution_count": 112,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "xgb_reg = xgb.XGBRegressor(n_estimators=300, learning_rate=0.1, random_state=42)\n",
    "xgb_reg.fit(X_train_scaled, y_train)\n",
    "y_pred_xgb_reg = xgb_reg.predict(X_test_scaled)\n",
    "r2_score(y_test, y_pred_xgb_reg)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 114,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.8068464937860642"
      ]
     },
     "execution_count": 114,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.16"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
