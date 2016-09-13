package nctu.fintech.db;

import android.support.annotation.NonNull;
import android.util.Log;

import org.json.JSONArray;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.UnsupportedEncodingException;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLEncoder;
import java.util.Map;

/**
 * SQL connect, client side
 *
 * 已實作功能:
 * <ol>
 *     <li>Get: 取得全部物件</li>
 *     <li>Get: 依索引值取得特定物件</li>
 *     <li>Get: 依索篩選器取得特定物件 (尚無法使用進階篩選)</li>
 *     <li>Put: 新增一個物件</li>
 *     <li>Update: 更新一個物件</li>
 *     <li>Delete: 刪除一個物件</li>
 * </ol>
 *
 * @version 0.9.0 (2016-09-12)
 * @author  Tzu-ting, NCTU Fintech Center
 */
public class DbAdapter {

    //*******************************************************
    //  Constants
    //
    //*******************************************************
    private final String BASE_URL = "http://localhost:8000/api";           // 基底網址, 注意尾部的'/'不用加
    private final String CONTENT_TYPE = "application/x-www-form-urlencoded";    // Request Content-type
    private final String ENCODE = "utf-8";                                      // Encoding

    //*******************************************************
    //  Private fields
    //
    //*******************************************************
    private String _db;

    //*******************************************************
    //  Constructor
    //
    //*******************************************************
    /**
     * 建構子, 建立資料庫連線
     * @param selected_db 要連接的資料庫
     */
    public DbAdapter(String selected_db) {
        if (selected_db == null || selected_db.isEmpty())
        {
            throw new IllegalArgumentException();
        }
        _db = selected_db;
    }

    //*******************************************************
    //  Public members
    //
    //*******************************************************
    /**
     * 取得所有清單
     * @return 資料庫上的所有資料, 連線失敗時回傳null
     */
    public JSONArray Get() {
        JSONArray array = null;
        try {
            URL url = new URL(String.format("%s/%s/?format=json", BASE_URL, _db));

            HttpURLConnection con = initConnection("GET", url, false);
            int code = con.getResponseCode();
            if (code != HttpURLConnection.HTTP_OK)
            {
                Log.w(this.getClass().getName(), "Unexpected response code: " + code);
                return null;
            }

            String content = getResponse(con);
            array = new JSONArray(content);

        } catch (Exception e) {
            Log.e(this.getClass().getName(), e.getMessage());
        }

        return array;
    }

    /**
     * 取得特定物件
     * @param index 物件索引
     * @return 指定的物件, 找不到或連線失敗時回傳null
     */
    public JSONObject Get(int index) {
        JSONObject obj = null;
        try {
            URL url = new URL(String.format("%s/%s/%d/?format=json", BASE_URL, _db, index));

            HttpURLConnection con = initConnection("GET", url, false);
            int code = con.getResponseCode();
            if (code != HttpURLConnection.HTTP_OK)
            {
                Log.w(this.getClass().getName(), "Unexpected response code: " + code);
                return null;
            }

            String content = getResponse(con);
            obj = new JSONObject(content);

        } catch (Exception e) {
            Log.e(this.getClass().getName(), e.getMessage());
        }
        return obj;
    }

    /**
     * 取得符合條件的物件清單
     * @param filter 篩選條件
     * @return 指定的物件, 找不到或連線失敗時回傳null
     */
    public JSONArray Get(String filter) {
        JSONArray array = null;
        try {
            URL url = new URL(String.format("%s/%s/?%s&format=json", BASE_URL, _db, filter));

            HttpURLConnection con = initConnection("GET", url, false);
            int code = con.getResponseCode();
            if (code != HttpURLConnection.HTTP_OK)
            {
                Log.w(this.getClass().getName(), "Unexpected response code: " + code);
                return null;
            }

            String content = getResponse(con);
            array = new JSONArray(content);

        } catch (Exception e) {
            Log.e(this.getClass().getName(), e.getMessage());
        }

        return array;
    }

    /**
     * 新增一個物件
     * @param data 以Map<,>標示
     * @return 成功與否
     */
    public boolean Put(Map<String, String> data) {
        try {
            URL url = new URL(String.format("%s/%s/?format=json", BASE_URL, _db));

            HttpURLConnection con = initConnection("POST", url, true);

            String param = encodeParam(data);
            outputData(con, param);

            int code = con.getResponseCode();
            if (code != HttpURLConnection.HTTP_CREATED)
            {
                Log.w(this.getClass().getName(), "Unexpected response code: " + code);
                return false;
            }
        } catch (Exception e) {
            Log.e(this.getClass().getName(), e.getMessage());
        }
        return true;
    }

    /**
     * 更新欄位
     * @param index 要更新的物件
     * @param changes 變動的欄位(key)與內容(value)
     * @return 成功與否
     */
    public boolean Update(int index, Map<String, String> changes) {
        try {
            URL url = new URL(String.format("%s/%s/%d/?format=json", BASE_URL, _db, index));

            HttpURLConnection con = initConnection("PUT", url, true);

            String param = encodeParam(changes);
            outputData(con, param);

            int code = con.getResponseCode();
            if (code != HttpURLConnection.HTTP_OK)
            {
                Log.w(this.getClass().getName(), "Unexpected response code: " + code);
                return false;
            }
        } catch (Exception e) {
            Log.e(this.getClass().getName(), e.getMessage());
        }
        return true;
    }

    /**
     * 刪除一個物件
     * @param index 要刪除的物件
     * @return 成功與否
     */
    public boolean Delete(int index) {
        try {
            URL url = new URL(String.format("%s/%s/%d/?format=json", BASE_URL, _db, index));

            HttpURLConnection con = initConnection("DELETE", url, false);

            int code = con.getResponseCode();
            if (code != HttpURLConnection.HTTP_NO_CONTENT)
            {
                Log.w(this.getClass().getName(), "Unexpected response code: " + code);
                return false;
            }
        } catch (Exception e) {
            Log.e(this.getClass().getName(), e.getMessage());
        }
        return true;
    }

    //*******************************************************
    //  Private members
    //
    //*******************************************************
    /**
     * initialize a connection
     * @param method  request method
     * @param url request target
     * @param hasOutputData to upload data or not
     * @return http connector
     * @throws IOException
     */
    private HttpURLConnection initConnection(String method, URL url, boolean hasOutputData) throws IOException
    {
        // 紀錄
        Log.v(this.getClass().getName(), String.format("Proceed %s %s", method, url));

        // 開啟連線
        HttpURLConnection con = (HttpURLConnection) url.openConnection();
        con.setRequestMethod(method);

        // 設定上傳標頭
        if (hasOutputData) {
            con.setRequestProperty("content-type", CONTENT_TYPE);
            con.setDoOutput(true);
        }

        return con;
    }

    /**
     * upload data
     * @param con http connector
     * @param data encoded parameters
     * @throws IOException
     */
    private void outputData(HttpURLConnection con, String data) throws IOException
    {
        try (DataOutputStream writer = new DataOutputStream(con.getOutputStream())) {
            writer.writeBytes(data);
        }
    }

    /**
     * get response data
     * @param con http connector
     * @return response result
     * @throws IOException
     */
    private String getResponse(HttpURLConnection con) throws IOException
    {
        StringBuilder builder = new StringBuilder();
        try (BufferedReader reader = new BufferedReader(new InputStreamReader(con.getInputStream())))
        {
            String in;
            while ((in = reader.readLine()) != null) {
                builder.append(in);
            }
        }

        // return result
        return builder.toString();
    }

    /**
     * encode parameter set
     * @param param_set parameter set
     * @return encoded string
     */
    @NonNull
    private String encodeParam(Map<String, String> param_set) throws UnsupportedEncodingException
    {
        StringBuilder params = new StringBuilder();
        Boolean isFirst = true;
        for (Map.Entry<String, String> pair : param_set.entrySet()) {
            if (!isFirst)
            {
                params.append("&");
            }

            params.append(URLEncoder.encode(pair.getKey(), ENCODE));
            params.append("=");
            params.append(URLEncoder.encode(pair.getValue(), ENCODE));

            isFirst = false;
        }
        return  params.toString();
    }

}
