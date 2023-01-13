import { Article } from "@/modules/types";
import { author } from "@/modules/controllers";

export class ArticleController {
    async write(writtenData: Article) : Promise<any> {
        try {
            await author.post('/Article', writtenData)
        } catch (error) {
            return error;
        }
    }

}