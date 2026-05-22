import json
with open (r'C:\Users\RAKESH KUMAR DAS\myntra_project\myntra_data.json', 'r',encoding="utf-8") as file:
    data=json.load(file)

product_name=(data['pdpData']['name'])

product_code=(data['pdpData']['id'])

product_mrp=(data['pdpData']['price']['mrp'])

discounted_mrp=(data['pdpData']['price']['discounted'])

discount_per=((product_mrp-discounted_mrp)/product_mrp)*100
discount_per=float(f"{discount_per:.2f}")

raw_rating_info=data['pdpData']['ratings']['ratingInfo']
formatted_list={str(item['rating']):item['count'] for item in raw_rating_info}
sorted_rating_info=dict(sorted(formatted_list.items(), key=lambda x: int(x[0]), reverse=True))

no_of_ratings=(data['pdpData']['ratings']['totalCount'])

raw_avg_ratings=(data['pdpData']['ratings']['averageRating'])

avg_ratings=float(f"{raw_avg_ratings:.2f}")

raw_sizes=data['pdpData'].get('sizes', [])
size_status= []
for size_item in raw_sizes:
    size_status.append({
        "label": size_item.get('label', 'N/A' ),
        "isAvailable": size_item.get('available', False)
    })

seller_name=data['pdpData'].get('sellers', [{}])[0].get('sellerName', 'N/A')

specifications=data['pdpData'].get('articleAttributes', [])
product_specifications = {
    "product_code": str(product_code),
    "lenght": data['pdpData']['articleAttributes'].get('Length', 'N/A'),
    "neck style": data['pdpData']['articleAttributes'].get('Neck', 'N/A'),
    "fabric_info": data['pdpData']['articleAttributes'].get('Fabrics', 'N/A'),
    "fashion_trends": data['pdpData']['articleAttributes'].get('Fashion Trends', 'N/A'),
    "wash_care": data['pdpData']['articleAttributes'].get('Wash Care', 'N/A'),
    "transparency":None,
    "number_of_items": int(data['pdpData']['articleAttributes'].get('Number of Items', 'N/A'))
    }



output_data={
    "product_name": product_name,
    "product_code": product_code,
    "product_mrp": product_mrp,
    "discounted_mrp": discounted_mrp,
    "discount_per": discount_per,
    "rating_info": sorted_rating_info,
    "ratings": no_of_ratings,
    "avg_ratings": avg_ratings,
    "size_status": size_status,
    "seller_name": seller_name,
    "product_specifications": product_specifications,
}
print(json.dumps(output_data, indent=4))
output_file_path=r'C:\Users\RAKESH KUMAR DAS\myntra_project\output.json'
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    json.dump(output_data, output_file, indent=4, ensure_ascii=False)
print(f"Data has been successfully written to {output_file_path}")
